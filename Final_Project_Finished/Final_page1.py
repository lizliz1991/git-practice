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

#Make the output list
    output =[]

#Combine the root url with the list 
    root_url = "https://www.como.gov/CMS/health_inspections/"
    inspection = urlparse.urljoin(root_url, list)
    #print inspection

#Read each url 
    inspection_page = requests.get(inspection)
    soup = BeautifulSoup(inspection_page.content, "html.parser")

#Get the text I need; replace the tag I don't want and change the delimitor into comma
    for basic in soup.find_all('div', attrs={'class':'establishmentinfo'}):
        result = basic.get_text().encode('utf-8')
        result1 = result.replace('\nEstablishment:','').replace('\nType:',',').replace('\n','')
        result2 = result1.replace('-',',')
        #info = [str(result)]
        output.append(str(result2))
        

    for inspec_info in soup.find('div', attrs={'class':'inspectionheader'}):
        inspection_result = inspec_info.get_text().encode('utf-8')
        inspection_result1 = inspection_result.replace('Inspection Date:','').replace('Type:','').replace('Comments:','').replace('Critical Violations:','').replace('Non-Critical Violations:','').replace('\n','')
        inspection_result2 = inspection_result1.replace('Non-','')
        #inspection_info = [str(inspection_result)]
        output.append(str(inspection_result2))

    print output


        

    


    
