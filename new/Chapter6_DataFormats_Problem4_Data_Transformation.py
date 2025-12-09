import csv
import json

def csv_to_json(csv_file, json_file):
    data = {"people": []}
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['Age'] = int(row['Age'])
            data["people"].append(row)
    with open(json_file, 'w') as f:
        json.dump(data, f)

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows([['Name', 'Age', 'City'], ['Ali', 25, 'Cairo'], ['Mona', 30, 'Alex']])

csv_to_json('data.csv', 'data.json')
