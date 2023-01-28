import csv

original_file = 'customers.csv'
new_file = 'customers_country.csv'

infile = open(original_file, 'r',)
outfile = open(new_file, 'w')

reader = csv.reader(infile)
writer = csv.writer(outfile, delimiter=',')

next(reader)

for row in reader:
    fn = row[1]
    ln = row[2]
    city = row[3]
    country = row[4]
    phone = row[5]
    
    writer.writerow([fn,ln,country])

infile.close()
outfile.close()


