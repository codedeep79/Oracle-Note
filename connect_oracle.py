from __future__ import print_function

import cx_Oracle

# User hr
# Password welcome 
# Database name is testoracledb
connection = cx_Oracle.connect("hr", "welcome", "localhost/testoracledb")

cursor = connection.cursor()
cursor.execute("""
    SELECT first_name, last_name
    FROM employees
    WHERE department_id = :did AND employee_id > :eid""",
    did = 50,
    eid = 190)
for fname, lname in cursor:
    print("Values:", fname, lname)
