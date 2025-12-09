import csv

with open('students.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows([['ID', 'Name', 'Grade'], [1, 'Ali', 85], [2, 'Mona', 92], [3, 'Omar', 78]])

with open('students.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row['Grade']) > 80:
            print(row['Name'])
