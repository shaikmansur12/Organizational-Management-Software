# database_setup.py
import sqlite3

def create_database():
    conn = sqlite3.connect("Employee_DataBase1.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Department (
                        Dept_id INTEGER,
                        name TEXT,
                        location TEXT,
                        manager TEXT,
                        dept_name TEXT,
                        emp_id INTEGER,
                        FOREIGN KEY (emp_id) REFERENCES Employee(Emp_id)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Employee (
                        Emp_id INTEGER PRIMARY KEY,
                        name TEXT,
                        age INTEGER,
                        doj TEXT,
                        email TEXT,
                        gender TEXT,
                        contact TEXT,
                        address TEXT,
                        department_id INTEGER
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Project (
                        P_id INTEGER PRIMARY KEY,
                        name TEXT,
                        start_date TEXT,
                        end_date TEXT,
                        employee_id INTEGER,
                        department_id INTEGER,
                        FOREIGN KEY (employee_id) REFERENCES Employee(Emp_id)
                    )''')

    conn.commit()
    conn.close()
