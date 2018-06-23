from requests import *
from bs4 import BeautifulSoup

import pandas as pd

url = 'https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168'

response=get(url)
# print(response.text[:500])
soup=BeautifulSoup(response.content, 'html.parser')
seven_day=soup.find(id='seven-day-forecast')

periods=[p.get_text() for p in seven_day.select(".tombstone-container .period-name")]
temps=[t.get_text() for t in seven_day.select(".tombstone-container .temp")]
short_descs= [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
descs=[d["title"] for d in seven_day.select(".tombstone-container img")]


print(periods)
print(" ")
print (short_descs)
print(" ")soup=bs4.BeautifulSoup(data.text)


print(temps)
print(" ")

print(descs)

weather = pd.DataFrame({
    "period":periods,
    "short_desc":short_descs,
    "temp":temps,
    "desc":descs,
})
temp_nums=weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"]=temp_nums.astype('int')
weather.to_csv('weather.csv')

print (temp_nums)
print (weather)