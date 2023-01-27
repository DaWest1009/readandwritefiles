import csv

infile = open('customers.csv','r',newline='')
reader = csv.reader(infile)
labels = next(reader)

#print('\n    ', labels[0], labels[1], labels[2],
#          '\n    ', '-' * 7, '-' * 10, '-' * 10)
print("Hey")

