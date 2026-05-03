import sqlite3

class HospitalDB:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def get_patients(self):
        print("\n[Patient Table]\n")
        self.cursor.execute("SELECT * FROM PATIENT")
        rows = self.cursor.fetchall()

        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} {row[2]} | DOB: {row[3]} | Phone: {row[4]} | Bed: {row[5]}")

    def get_employees(self):
        print("\n[Employee Table]\n")
        self.cursor.execute("SELECT * FROM EMPLOYEE")
        rows = self.cursor.fetchall()

        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} {row[2]} | Job: {row[3]} | Salary: ${row[4]}")

    def close(self):
        self.connection.close()

db = HospitalDB("C:/Users/braed/Desktop/School/Compilation/Database Systems/hospital.db")

db.get_patients()
db.get_employees()
db.close()