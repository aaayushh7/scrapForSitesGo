import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://med.stanford.edu/neurology/faculty/overview.html?tab=proxy"

html = requests.get(url)
# print(html)  status 200

soup = BeautifulSoup(html.text, "html.parser")
# print(soup) recieved html.text

main_parsys = soup.find('div', class_ = "main parsys")
# print(main_parsys)
imageURL=[]
Allnames =[]
Allmails=[]
Links=[]
#   LEFT PANEL
panelLeft = main_parsys.find('div', class_ = 'col-sm-4 panel-builder-33-col panel-builder-left')
image = panelLeft.find('div', class_ = 'image' )
img_tag = image.find('img')
img_src = img_tag.get('src','')
divName = panelLeft.find('div', class_ = 'text col-md-8')
innerDivName = divName.find('p').find('a')
name = innerDivName.get_text(strip=True)
# print(name)
Allnames.append(name)
# print(img_src)
imageURL.append(img_src)
innerLink = main_parsys.find('a', href=True)
innerURL = innerLink['href']
# print(innerURL)
Links.append(innerURL)
innerResponse = requests.get(innerURL)
innerSoup = BeautifulSoup(innerResponse.text, 'html.parser')

contact = innerSoup.find('div', 'contact-info primary')
if contact:

    contact2 = contact.find('a')
    email = contact2.get_text(strip=True)
    # print(email)
    Allmails.append(email)
else:
    Allmails.append("Not Found")
# innerResponse = requests.get(innerURL)
# innerSoup = BeautifulSoup(innerResponse.text, 'html.parser')
# print(innerSoup)

#MIDPANEL
panelMid = main_parsys.find('div', class_='col-sm-4 panel-builder-33-col panel-builder-mid')
image = panelMid.find('div', class_ = 'image' )
img_tag = image.find('img')
img_src = img_tag.get('src','')
divName = panelMid.find('div', class_ = 'text col-md-8')
innerDivName = divName.find('p').find('a')
name = innerDivName.get_text(strip=True)
# print(name)
Allnames.append(name)
# print(img_src)
imageURL.append(img_src)
innerLink = panelMid.find('a', href=True)
innerURL = innerLink['href']
# print(innerURL)
Links.append(innerURL)
innerResponse = requests.get(innerURL)
innerSoup = BeautifulSoup(innerResponse.text, 'html.parser')
contact = innerSoup.find('div', 'contact-info primary')
contact2 = contact.find('a')
email = contact2.get_text(strip=True)
# print(email)
Allmails.append(email)


#  RIGHTPANEL
panelRight = main_parsys.find('div', class_='col-sm-4 panel-builder-33-col panel-builder-right')
divName = panelRight.find('div', class_ = 'text col-md-8')
innerDivName = divName.find('p').find('a')
name = innerDivName.get_text(strip=True)
# print(name)
Allnames.append(name)
innerLink = panelRight.find('a', href=True)
innerURL = innerLink['href']
# print(innerURL)
Links.append(innerURL)
innerResponse = requests.get(innerURL)
innerSoup = BeautifulSoup(innerResponse.text, 'html.parser')

contact = innerSoup.find('div', 'contact-info primary')
if contact:

    contact2 = contact.find('a')
    email = contact2.get_text(strip=True)
    # print(email)
    Allmails.append(email)
else:
    Allmails.append("Not Found")

print("All mails : ", Allmails)
print("Name : ", Allnames)
print("URL to profile : ", Links)