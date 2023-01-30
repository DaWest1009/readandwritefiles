import csv

original_file = 'sales.csv'
new_file = 'salesreport.csv'

infile = open(original_file, 'r',)
outfile = open(new_file, 'w')

reader = csv.reader(infile)
writer = csv.writer(outfile, delimiter=',')

fieldnames = next(reader)
fieldnames[1] = 'Total'
newfields = (fieldnames[0], fieldnames[1])
writer.writerow(newfields)

count = 0
last_cust = ''
total = 0

for row in reader:
    cust_id = row[0]
    subtotal = float(row[3])
    tax = float(row[4])
    freight = float(row[5])
    if count == 0:
        last_cust = cust_id
    if cust_id  == last_cust:
        total += subtotal + tax + freight
    else:
        writer.writerow((last_cust, format (total, '.2f')))
        total = subtotal + tax + freight
    last_cust = cust_id
    count += 1
writer.writerow((last_cust, format (total, '.2f')))


infile.close()
outfile.close()
