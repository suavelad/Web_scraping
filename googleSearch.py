"""
This Program recieves google search keyword through commandline arguments.
Example: googleSearch.py What is Data Science
Then it opens the web browser and opens the related search result links 
on different tabs
"""

import webbrowser, sys, requests,bs4

# def search():
#     try:
keyword= ''.join(sys.argv[1:])
print("Is the keyword : " + keyword + "?")
reply= input("Y or N >> ")

if (reply.upper() =="Y"):
    pass


elif (reply.upper() == "N"):
    print ("Insert the Keyword below")
    keyword= input("The KeyWord >> ")
    keyword=keyword.replace(' ','')
    print (keyword)
    



else:
    print("Wrong Input ")
    exit() 

data=requests.get("https://google.com/search?q="+ keyword)

data.raise_for_status()
# Try the comment part
# soup=bs4.BeautifulSoup(data)
soup=bs4.BeautifulSoup(data.text)
# links = soup.select('.r a').gettext()
print('Your Browser is opening ...')
links = soup.select('.r a')
webbrowser.open("https://google.com/search?q="+ keyword)

for link in links:
    webbrowser.open('https://google.com'+link.get('href'))           
            
#     except Exception as e:
#         print("The Problem is : %s" %(e))

# search()
