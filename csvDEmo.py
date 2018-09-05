import csv

with open('csvDemo.csv') as csvfile:
    reader=csv.reader(csvfile)
    rows=[row for row in reader]
print(rows)

