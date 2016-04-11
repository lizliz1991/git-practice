#coding: utf-8
import os, sys
import urllib2, csv
import mechanize
from bs4 import BeautifulSoup 

# Create the output file
output = open('output.csv','w')
writer = csv.writer(output)
writer.writerow(['county', 'clinton_pct', 'sanders_pct', 'cruz_pct', 'kasich_pct', 'trump_pct'])

br = mechanize.Browser()
br. open('http://enr.sos.mo.gov/EnrNet/CountyResults.aspx')

# Get HTML
html = br.response().read()

#Transform the HTML into a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

#Find the county list
countylist = soup.find('select', {'name':'ctl00$MainContent$cboCounty', 'id': 'cboCounty'}).find_all('option')

# Fill out the form
for county in countylist:
    county_id = county['value']

    br.select_form(nr=0)
    br.form['ctl00$MainContent$cboElectionNames'] = ['750003566']
    br.form['ctl00$MainContent$cboCounty'] = [county_id]

# Submit the form
    br.submit('ctl00$MainContent$btnCountyChange')

#Get HTML
    html = br.response().read()

#Transform the HTML into a BeautifulSoup object
    soup = BeautifulSoup(html, "html.parser")

#Find the main table
    main_table = soup.find('table', 
    {'id': 'MainContent_dgrdResults'}
    )

#Define final list--select_data
    select_data = []
    select_data.append(county.text)

#Get the data from each table row
    for row in main_table.find_all('tr'):
        data = [cell.text for cell in row.find_all('td')]

#Select candidates
        name = ['Hillary Clinton', 'Bernie Sanders', 'Ted Cruz', 'John R. Kasich','Donald J. Trump']
        for data[0] in data:
            if data[0] in name:
                select_data.append(data[3]) 

    print select_data
    writer. writerow(select_data)   
