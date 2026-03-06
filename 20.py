import csv

with open("employee.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        emp_id, name, salary = row
        if int(salary) > 50000:
            print(emp_id, name, salary)