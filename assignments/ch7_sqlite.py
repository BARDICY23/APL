import sqlite3
def setup_db(path='school.db'):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY, name TEXT, grade REAL)')
    conn.commit()
    return conn
def insert_student(conn, name, grade):
    cur = conn.cursor()
    cur.execute('INSERT INTO students(name, grade) VALUES(?, ?)', (name, grade))
    conn.commit()
def get_all(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM students')
    return cur.fetchall()
def transactional_example(path='school.db'):
    conn = sqlite3.connect(path)
    try:
        cur = conn.cursor()
        cur.execute('BEGIN')
        cur.execute('INSERT INTO students(name, grade) VALUES(?, ?)', ('T1', 50))
        cur.execute('INSERT INTO students(name, grade) VALUES(?, ?)', ('T2', 60))
        1/0
        conn.commit()
    except Exception as e:
        conn.rollback()
        print('Transaction rolled back.')
    finally:
        conn.close()
if __name__ == '__main__':
    conn = setup_db()
    insert_student(conn, 'Ali', 85.5)
    insert_student(conn, 'Sara', 92.0)
    insert_student(conn, 'Mohamed', 78.3)
    print(get_all(conn))
    conn.close()
    transactional_example()
