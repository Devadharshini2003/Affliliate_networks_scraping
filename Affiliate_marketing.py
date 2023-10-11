import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium import webdriver
#import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

first = webdriver.Chrome()
base_address="https://www.affpaying.com"
#conform='https://www.offervault.com/networks/?search=&page=14'
conform='https://www.affpaying.com/affiliate-networks'
first.get(conform)  #for opening the connections page
time.sleep(4)
connections = first.page_source #variable and assigning the source code in first variable

soup = BeautifulSoup(connections, 'html.parser')
#act = soup.find_all('div',"class_").prettify()
#name = soup.find('div',{'class': 'flex-col pb-4'}).prettify()
#print(name)

#current=soup.find('a',{'class':'text-blue-dark no-underline hover:text-orange'}).get_text()
#print(current)

anchor_tags = soup.find_all("a",{'class':"text-blue-dark no-underline hover:text-orange"})
company_name=[]
# Loop through the anchor tags and extract the text
for tag in anchor_tags:
    text = tag.text
    company_name.append(text)
print(company_name)

company_offers=[]
offers = soup.find_all("a",{'class':"text-blue-dark border-b border-blue-lighter"})
for tag in offers:
    text = tag.text
    if "Offers" in text:
        company_offers.append(text)
print(company_offers)

company_links=[]
links=soup.find_all("a",{'class':"text-blue-dark no-underline hover:text-orange"})
for tag in links:
   # print(base_address+tag['href'])
    copy=base_address+tag['href']
    company_links.append(copy)
print(company_links)


