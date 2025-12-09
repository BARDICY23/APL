import json

data = {"course": "Python", "duration": "3 months", "students": ["Ali", "Sara"]}

with open('course.json', 'w') as f:
    json.dump(data, f)

with open('course.json', 'r') as f:
    loaded = json.load(f)
    print(loaded['students'])
