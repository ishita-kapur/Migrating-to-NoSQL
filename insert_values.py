# Ishita Kapur, UTA ID: 1001753123
import csv
import mysql.connector

# establish a connection with the MySQL server
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="db2",
  auth_plugin='mysql_native_password'
)

# create a MySQL cursor object
mycursor = mydb.cursor()

print('\nINSERTING VALUES INTO DEPARTMENT')

query = "insert into department values(%s, %s, %s, %s)"
with open('csv files/department.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        for i in range(len(row)):
            if row[i] == '':
                row[i] = None
        print(row)
        # executes the query using the execute() method
        mycursor.execute(query, row)
csvfile.close()

print('\nINSERTING VALUES INTO EMPLOYEE')

query = "insert into employee values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
with open('csv files/employee.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        for i in range(len(row)):
            if row[i] == '':
                row[i] = None
        print(row)
        mycursor.execute(query, row)
csvfile.close()

print('\nINSERTING VALUES INTO PROJECT')

query = "insert into project values(%s, %s, %s, %s)"
with open('csv files/project.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        for i in range(len(row)):
            if row[i] == '':
                row[i] = None
        print(row)
        mycursor.execute(query, row)
csvfile.close()

print('\nINSERTING VALUES INTO WORKS_ON')

query = "insert into works_on values(%s, %s, %s)"
with open('csv files/works_on.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        for i in range(len(row)):
            if row[i] == '':
                row[i] = None
        print(row)
        mycursor.execute(query, row)
csvfile.close()

# commit the changes to the database
mydb.commit()