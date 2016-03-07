import csv

csvfile = open('./cleanme.csv', 'r')
outfile = open('./clean_data.csv', 'w')

reader = csv.DictReader(csvfile)
writer = csv.DictWriter(outfile, reader.fieldnames)

writer.writeheader()

#Uppercase 
for row in reader:
    row['first_name'] = row['first_name'].upper()
    row['city'] = row['city'].upper()
    row['last_name'] = row['last_name'].upper()
    row['freport_id'] = row['freport_id'].upper()
    row['transaction_code'] = row['transaction_code'].upper()
    row['contrib_code'] = row['contrib_code'].upper()
    row['mid_init'] = row['mid_init'].upper()
    row['addr'] = row['addr'].upper()
    row['state'] = row['state'].upper()
    row['filer_id'] = row['filer_id'].upper()
#Add leading zero
    row['zip'] = row['zip'].zfill(5)
#Delete
    row['city'] = row['city'].replace("&NBSP;", "")  
#contributions of 1,000 or more 
    if int(row['amount']) >= 1000: 
    
        print row 
        writer. writerow(row)




