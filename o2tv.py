"""
This python script check latest series uploaded
then it will check if any of the ones in my movie list
is there, finally it will navigate to the download page
and download it.

Author: Sunday Ajayi
"""
#! usr/bin/python3

import requests, bs4
from selenium import webdriver

# browser=webdriver.Firefox()
def scrape():
    try:
        lists=['The 100','The Blacklist','Riverdale', 'Blindspot','Quantico']

        main_webpage= requests.get('http://o2tvseries.com')
        main_soup=bs4.BeautifulSoup(main_webpage.content,'html.parser')

        recents= main_soup.findAll("div",{"class":'data main'})
        for recent in recents:
            for list in lists:
                if recent.find('b').text==list:
                    print (list)
                    # Series Page
                    print('The link is : http://o2tvseries.com/'+list[0].lower())
                    series_webpage=requests.get('http://o2tvseries.com/'+list[0].lower())
                    series_soup=bs4.BeautifulSoup(series_webpage.content,'html.parser')
                    pages=series_soup.findAll("div",{"class":'data'})
                    for page in pages:
                        for list in lists:
                            if page.a.text ==list:
                                print (page.a['href'])
                                # navigate to the seasons Page
                                seasons_webpage=requests.get(page.a['href'])
                                seasons_soup=bs4.BeautifulSoup(seasons_webpage.content,'html.parser')
                                seasons=seasons_soup.findAll("div",{"class":"data"})

                                # Navigate to the latest season page
                                latest_season_webpage =requests.get(seasons[0].a['href'])
                                latest_season_soup=bs4.BeautifulSoup(latest_season_webpage.content,'html.parser')
                                latest_season=latest_season_soup.findAll("div",{"class":'data'})

                                # Navigate to the latest episode page
                                latest_episode_webpage =requests.get(seasons[0].a['href'])
                                latest_episode_soup=bs4.BeautifulSoup(latest_episode_webpage.content,'html.parser')
                                latest_episode=latest_episode_soup.findAll("div",{"class":'data'})
                                print(latest_episode[0].a.text)
                                print(latest_episode[0].a['href'])
                                print('**************')

                                # navigate to the video quality type page
                                videos_webpage =requests.get(latest_episode[0].a['href'])
                                videos_soup=bs4.BeautifulSoup(videos_webpage.content,'html.parser')
                                videos=videos_soup.findAll("div",{"class":'data'})
                                for video in videos:
                                    if 'HD' in video.a.text:
                                        print(video.a.text+':'+video.a['href'])
                                        print("****Browser is being opened*****")
                                        browser=webdriver.Firefox()
                                        browser.get(video.a['href'])
                                        browser.find_element_by_class_name("g-recaptcha").click
                                        # browser.find_element_by_xpath(".//*[contains(text(),'I\'m not a robot')]").click()
                                        # browser.find_element_by_xpath("//input[@type='submit']").click
                                        browser.find_element_by_name("submit").click
                        



                                    
                                


                            
                                print(videos[0].a.text)
                                print(videos[0].a['href'])

                                print(videos[0].a.text)
                                print(videos[0].a['href'])

                                for season in seasons:
                                    print(season.a.text)
                                    print(season.a['href'])
                            
                        print(page.a.text)

                    print("***********")
        else:
            print ("You Do not have an update yet")        

    except Exception as e:
        print('The Error is : %s'%(e))


scrape()
