import requests
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_formatting import *
import re


scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
credentials = ServiceAccountCredentials.from_json_keyfile_name("/Users/ayushtiwari/PycharmProjects/sitesGo/secretkey.json", scope)
client = gspread.authorize(credentials)
spreadsheet = client.open('SitesGo')
sheet = spreadsheet.sheet1


url = "https://med.stanford.edu/neurology/faculty/overview.html?tab=proxy"

html = requests.get(url)
# print(html)  status 200

soup = BeautifulSoup(html.text, "html.parser")
# print(soup) recieved html.text

main_parsys = soup.find('div', class_ = "main parsys")
# print(main_parsys)
# imageURL=[]
Allnames =[]
Allmails=[]
# Links=[]
Lab=[]

#   SCRAPING FUNCTION USING PREVIOUS LINES (110-193)

def scrape_panel(panel):
    for panel_item in panel:
        div_name = panel_item.find('div', class_='text col-md-8')
        if div_name:
            p_tag = div_name.find('p')
            if p_tag:
                inner_div_name = p_tag.find('a') or p_tag
                name = inner_div_name.get_text(strip=True)
                Allnames.append(name)
            else:
                continue

            inner_link = panel_item.find('a', href=True)
            if inner_link:
                inner_url = inner_link['href']
                # Links.append(inner_url)

                try:
                    inner_response = requests.get(inner_url)
                    inner_soup = BeautifulSoup(inner_response.text, 'html.parser')
                    contact = inner_soup.find('div', 'contact-info primary')
                    internet_links = inner_soup.find_all('li', class_='internet-link')

                    if contact:
                        contact_email_tag = contact.find('a')
                        if contact_email_tag:
                            contact_email = contact_email_tag.get_text(strip=True)
                            Allmails.append(contact_email)
                        else:
                            Allmails.append("No Email in Contact Info")
                    else:
                        Allmails.append("No Contact Info")

                    lab_site_found = False
                    if internet_links:
                        for link_item in internet_links:
                            link_text = link_item.find('a').get_text(strip=True)
                            if re.search(r'\bLab Site\b', link_text):
                                lab_site_link = link_item.find('a')['href']
                                Lab.append(lab_site_link)
                                lab_site_found = True
                                break

                        if not lab_site_found:
                            Lab.append("No Lab Link Found")
                    else:
                        Lab.append("No Links Available")
                except Exception as e:
                    print(f"Error scraping inner page: {e}")
            else:
                # Links.append("N/A")
                Allmails.append("N/A")
                Lab.append("N/A")
        else:
            print("No matching div found in this panel.")

panel_left = main_parsys.findAll('div', class_='col-sm-4 panel-builder-33-col panel-builder-left')
panel_mid = main_parsys.findAll('div', class_='col-sm-4 panel-builder-33-col panel-builder-mid')
panel_right = main_parsys.findAll('div', class_='col-sm-4 panel-builder-33-col panel-builder-right')

# Scrape each panel
scrape_panel(panel_left)
scrape_panel(panel_mid)
scrape_panel(panel_right)




print("All Panel : ", Allnames)
# print("All links : ", Links)
print("All emails : ", Allmails)
print("lab : ", Lab)

sheet.clear()
headers = ["Faculty Names", "Email", "Current Website"]
sheet.append_row(headers)
data = list(zip(Allnames, Allmails, Lab))
sheet.append_rows(data, value_input_option='USER_ENTERED')

#   FORMATING CELLS

# cell_range = sheet.range(f'A1:C{len(Allnames) + 1}')  # Including the header row
#
# # Apply formatting to cells
# for cell in cell_range:
#     if cell.row == 1:  # Header row
#         cell.color = (0.8, 0.8, 0.8)  # Gray background
#         cell.bold = True
#     elif cell.col == 2 or cell.col == 3:  # Email and URL columns
#         if not cell.value:
#             cell.color = (1, 0.8, 0.8)  # Red background
#
# # Update the formatted cells back to the sheet
# sheet.update_cells(cell_range)
# Get the entire range of cells


                                    ## PREVIOUS ROUGH LOGIC TO GET THE WORK DONE

# image = panelLeft.find('div', class_ = 'image' )
# img_tag = image.find('img')
# img_src = img_tag.get('src','')
# divName = panelLeft.find('div', class_ = 'text col-md-8')
# innerDivName = divName.find('p').find('a')
# name = innerDivName.get_text(strip=True)
# # print(name)
# Allnames.append(name)
# # print(img_src)
# # imageURL.append(img_src)
# innerLink = main_parsys.find('a', href=True)
# innerURL = innerLink['href']
# # print(innerURL)
# Links.append(innerURL)
# innerResponse = requests.get(innerURL)
# innerSoup = BeautifulSoup(innerResponse.text, 'html.parser')
#
# contact = innerSoup.find('div', 'contact-info primary')
# if contact:
#
#     contact2 = contact.find('a')
#     email = contact2.get_text(strip=True)
#     # print(email)
#     Allmails.append(email)
# else:
#     Allmails.append("Not Found")
# innerResponse = requests.get(innerURL)
# innerSoup = BeautifulSoup(innerResponse.text, 'html.parser')
# print(innerSoup)

#MIDPANEL
# panelMid = main_parsys.find('div', class_='col-sm-4 panel-builder-33-col panel-builder-mid')
# image = panelMid.find('div', class_ = 'image' )
# img_tag = image.find('img')
# img_src = img_tag.get('src','')
# divName = panelMid.find('div', class_ = 'text col-md-8')
# innerDivName = divName.find('p').find('a')
# name = innerDivName.get_text(strip=True)
# # print(name)
# Allnames.append(name)
# # print(img_src)
# imageURL.append(img_src)
# innerLink = panelMid.find('a', href=True)
# innerURL = innerLink['href']
# # print(innerURL)
# Links.append(innerURL)
# innerResponse = requests.get(innerURL)
# innerSoup = BeautifulSoup(innerResponse.text, 'html.parser')
# contact = innerSoup.find('div', 'contact-info primary')
# contact2 = contact.find('a')
# email = contact2.get_text(strip=True)
# # print(email)
# Allmails.append(email)


#  RIGHTPANEL
# panelRight = main_parsys.find('div', class_='col-sm-4 panel-builder-33-col panel-builder-right')
# divName = panelRight.find('div', class_ = 'text col-md-8')
# innerDivName = divName.find('p').find('a')
# name = innerDivName.get_text(strip=True)
# # print(name)
# Allnames.append(name)
# innerLink = panelRight.find('a', href=True)
# innerURL = innerLink['href']
# # print(innerURL)
# Links.append(innerURL)
# innerResponse = requests.get(innerURL)
# innerSoup = BeautifulSoup(innerResponse.text, 'html.parser')
#
# contact = innerSoup.find('div', 'contact-info primary')
# if contact:
#
#     contact2 = contact.find('a')
#     email = contact2.get_text(strip=True)
#     # print(email)
#     Allmails.append(email)
# else:
#     Allmails.append("Not Found")

# print("All mails : ", Allmails)
# print("Name : ", Allnames)
# print("URL to profile : ", Links)
