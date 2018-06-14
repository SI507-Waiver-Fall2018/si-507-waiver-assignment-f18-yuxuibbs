# these should be the only imports you need
import sys
import sqlite3

# write your code here
# usage should be 
#  python3 part2.py customers
#  python3 part2.py employees
#  python3 part2.py orders cust=<customer id>
#  python3 part2.py orders emp=<employee last name>
#


conn = sqlite3.connect("Northwind_small.sqlite")
cur = conn.cursor()

if len(sys.argv) < 3:
    if sys.argv[1] == "customers":
        cur.execute("SELECT id, ContactName FROM Customer")
        result = cur.fetchall()
        print("ID", "Customer Name")
        for customer in result:
            print(customer[0], customer[1])
    elif sys.argv[1] == "employees":
        cur.execute("SELECT id, LastName, FirstName FROM Employee")
        result = cur.fetchall()
        print("ID", "Employee Name")
        for customer in result:
            print(customer[0], customer[2], customer[1])
else:
    [command, search_term] = sys.argv[2].split("=")
    if command == "cust":
        print(search_term)
    elif command == "emp":
        pass