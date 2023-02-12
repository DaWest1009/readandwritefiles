import csv

infile = open('EmployeePay.csv', 'r')
reader = csv.reader(infile)
next(reader)

for row in reader:
    id = row[0]
    fn = row[1]
    ln = row[2]
    salary = row[3] 
    bonus = row[4]

    print('ID:', id)
    print('First Name:', fn)
    print('Last Name:', ln)
    print('Salary:', salary)
    print('Bonus:', bonus)
    print('Total Pay:', (float(salary) * float(bonus)) + float(salary))
    print('_'*20)

infile.close()