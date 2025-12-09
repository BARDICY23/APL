import sqlite3

conn = sqlite3.connect('school.db')
c = conn.cursor()

c.execute('''CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, grade REAL)''')
c.execute("INSERT INTO students VALUES (1, 'Ali', 85.5)")
c.execute("INSERT INTO students VALUES (2, 'Sara', 92.0)")
c.execute("INSERT INTO students VALUES (3, 'Mohamed', 78.3)")

conn.commit()

c.execute("SELECT * FROM students")
for row in c.fetchall():
    print(row)

conn.close()
