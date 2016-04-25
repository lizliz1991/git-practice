#coding: utf-8
import os, sys
import requests
import urlparse
from bs4 import BeautifulSoup

#Get the html
result = requests.get("https://www.como.gov/CMS/health_inspections/?type=RESTAURANT&keyword=&Submit=Search")

#Make it a BeautifulSoup object
soup = BeautifulSoup(result.content, "html.parser")

#Get the url lists
for link in soup.find(
    'div', attrs={'class':'inspectionlist'}).findChildren('a'):
    list = link['href']
    #print list 

#Combine the root url with the list 
    root_url = "https://www.como.gov/CMS/health_inspections/"
    inspection = urlparse.urljoin(root_url, list)
    #print inspection

#Read each url 
    inspection_page = requests.get(inspection)
    soup = BeautifulSoup(inspection_page.content, "html.parser")

#Get the text I need and turn the "Resultset" type to string
    for basic in soup.find_all('div', attrs={'class':'establishmentinfo'}):
        result = basic.get_text().encode('utf-8')
        info = [str(result)]
        print info

    for inspec_info in soup.find('div', attrs={'class':'inspectionheader'}):
        inspection_result = inspec_info.get_text().encode('utf-8')
        inspection_info = [str(inspection_result)]
        print inspection_info

    
    


    
