#Setting 
import urllib2, json, urllib

#Get the html
response = urllib2.urlopen('http://openstates.org/api/v1/bills/?apikey=1f366e0712bd4ad6b079afe3bb993434&state=mo&fields=title,sponsors').read()

bills = json.loads(response)

#Get the info
for bill in bills:
    encoded_bill_id = urllib.quote(bill['id'])
    bill_sponsors = urllib.unquote(bill['sponsors'][0]['name'])
    bill_title = urllib.unquote(bill['title'])

#print the info
    print encoded_bill_id, bill_sponsors, bill_title
    