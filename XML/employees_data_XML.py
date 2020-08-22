# Ishita Kapur, UTA ID: 1001753123
import json
import mysql.connector
from pprint import pprint
from pymongo import MongoClient
from dicttoxml import dicttoxml

## create a MongoClient to the running mongod instance
#client = MongoClient('localhost', 27017)
## access a database using dictionary style access
#db = client['company_db']
## access a collection using dictionary style access
#employees_projs = db['employees']

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

print('Fetching data from Relational Database')
query = "SELECT E.Lname, E.Fname, D.Dname, P.Pname, P.Pnumber, W.Hours FROM EMPLOYEE E, DEPARTMENT D, PROJECT P, WORKS_ON W WHERE P.Pnumber = W.Pno AND P.Dnum = E.Dno AND P.Dnum = D.Dnumber AND E.Dno = D.Dnumber AND E.Ssn = W.Essn"
# executes the query using the execute() method
mycursor.execute(query)

obj_arr = []
# reading data from the cursor row-wise
for lname, fname, dname, pname, pnumber, hours in mycursor:
  obj = {}
  obj['Lname'] = lname
  obj['Fname'] = fname
  obj['Dname'] = dname
  obj['Pname'] = pname
  obj['Pnumber'] = pnumber
  obj['Hours'] = float(hours)
  obj_arr.append(obj)

#print(obj_arr)

# creating a dictionary where key is a combination of LNAME, FNAME, DNAME
new_dict = {}

# iterating through the list
for item in obj_arr:
    try: # if the combination of LNAME, FNAME, DNAME already exists in the dictionary append the value of the dictionary with the combination of PNAME, PNUMBER, HOURS
        new_dict.get((item['Lname'], item['Fname'], item['Dname']))
        new_dict[(item['Lname'], item['Fname'], item['Dname'])].append({'Pname': item['Pname'], 'Pnumber': item['Pnumber'], 'Hours': item['Hours']})
    except KeyError: # if doesn't exist then create a new entry for the combination of LNAME, FNAME, DNAME
        new_dict[(item['Lname'], item['Fname'], item['Dname'])] = [{'Pname': item['Pname'], 'Pnumber': item['Pnumber'], 'Hours': item['Hours']}]

# pprint prints the data in a pretty format
#pprint(new_dict)

# create a list
new_list = []
for k, v in new_dict.items(): # keep appending dictionaries to the new list
    new_list.append({'Lname': k[0], 'Fname': k[1], 'Dname': k[2], 'Projects':list(v)})

pprint(new_list)

## convert a Python object into a JSON string using the dumps() method
#dictionary = json.dumps(new_list)
#pprint(dictionary)
#
#print('Sending to MongoDB')
## inserts each document in the list into the collection using the insert_many()
#results = employees_projs.insert_many(new_list)
## print list of _ids of the inserted documents
#print(results.inserted_ids)
## results in False if there is an invalid operation
#print(results.acknowledged)
#
## cleanup client resources and disconnect from MongoDB
#client.close()

xml = dicttoxml(new_list, custom_root='Employees', attr_type=False) # convert list to xml data

print(xml.decode("UTF-8"))

#with open("Employees.xml", "w") as f: # store xml data into a file
#    f.write(xml.decode("UTF-8"))

from xml.dom.minidom import parseString
dom = parseString(xml.decode("UTF-8"))
print(dom.toprettyxml())

with open("Employees.xml", "w") as f: # store xml data into a file
    f.write(dom.toprettyxml())