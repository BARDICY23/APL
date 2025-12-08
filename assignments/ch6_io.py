import csv
import json
import pandas as pd
def students_above_80(path):
    res = []
    with open(path, newline='') as f:
        r = csv.reader(f)
        next(r, None)
        for row in r:
            try:
                if float(row[2]) > 80:
                    res.append(row[1].strip())
            except:
                pass
    return res
def write_and_read_json(path):
    data = {"course": "Python", "duration": "3 months", "students": ["Ali", "Sara"]}
    with open(path, 'w') as f:
        json.dump(data, f)
    with open(path) as f:
        j = json.load(f)
    return j['students']
def excel_roundtrip():
    df = pd.DataFrame({'ID': [1,2], 'Name': ['A','B'], 'Salary':[1000,2000]})
    df.to_excel('employees.xlsx', index=False)
    df2 = pd.read_excel('employees.xlsx')
    return df2[['Name','Salary']]
def csv_to_json(inpath, outpath):
    people = []
    with open(inpath, newline='') as f:
        r = csv.DictReader(f)
        for row in r:
            people.append({'Name': row['Name'], 'Age': int(row['Age']), 'City': row['City']})
    with open(outpath, 'w') as f:
        json.dump({'people': people}, f)
if __name__ == '__main__':
    print(students_above_80('students.csv'))
    print(write_and_read_json('course.json'))
    print(excel_roundtrip())
