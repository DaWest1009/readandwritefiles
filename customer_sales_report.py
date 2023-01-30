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

for row in reader:
    cust_id = row[0]
    subtotal = float(row[3])
    tax = float(row[4])
    freight = float(row[5])
    total = subtotal + tax + freight
    newrow = [cust_id, total]
    writer.writerow(newrow)

infile.close()
outfile.close()