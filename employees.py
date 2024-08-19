# employees.py

from connector import Connector

class Employee:
    # Existing methods...

    @staticmethod
    def add_employee(emp_id, lname, fname, mname):
        try:
            query = "INSERT INTO employees (emp_id, lname, fname, mname) VALUES (%s, %s, %s, %s)"
            values = (emp_id, lname, fname, mname)

            Connector.cursor.execute(query, values)
            Connector.db.commit()

            return True
        except Exception as e:
            print("Error:", e)
            Connector.db.rollback()
            return False
