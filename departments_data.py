# Ishita Kapur, UTA ID: 1001753123
import json
import mysql.connector
from pprint import pprint
from pymongo import MongoClient

# create a MongoClient to the running mongod instance
client = MongoClient('localhost', 27017)
# access a database using dictionary style access
db = client['company_db']
# access a collection using dictionary style access
departments_emps = db['departments']

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
query = "SELECT D.Dname, D.Dnumber, M.Lname AS MGR_LNAME, M.Fname AS MGR_FNAME, E.Lname, E.Fname, E.Salary FROM DEPARTMENT D, EMPLOYEE M, EMPLOYEE E WHERE D.Dnumber = E.Dno AND D.Dnumber = M.Dno AND D.Mgr_ssn = M.Ssn ORDER BY D.Dname"
# executes the query using the execute() method
mycursor.execute(query)

obj_arr = []
# reading data from the cursor row-wise
for dname, dnumber, mgr_lname, mgr_fname, elname, efname, salary in mycursor:
  obj = {}
  obj['Dname'] = dname
  obj['Dnumber'] = dnumber
  obj['MGR_LNAME'] = mgr_lname
  obj['MGR_FNAME'] = mgr_fname
  obj['EMP_LNAME'] = elname
  obj['EMP_FNAME'] = efname
  obj['Salary'] = float(salary)
  obj_arr.append(obj)

#print(obj_arr)

# creating a dictionary where key is a combination of LNAME, FNAME, DNAME
new_dict = {}

# iterating through the list
for item in obj_arr:
    try: # if the combination of DNAME, DNUMBER, MGR_LNAME, MGR_FNAME already exists in the dictionary append the value of the dictionary with the combination of PNAME, PNUMBER, HOURS
        new_dict.get((item['Dname'], item['Dnumber'], item['MGR_LNAME'], item['MGR_FNAME']))
        new_dict[(item['Dname'], item['Dnumber'], item['MGR_LNAME'], item['MGR_FNAME'])].append({'EMP_LNAME': item['EMP_LNAME'], 'EMP_FNAME': item['EMP_FNAME'], 'Salary': item['Salary']})
    except KeyError: # if doesn't exist then create a new entry for the combination of DNAME, DNUMBER, MGR_LNAME, MGR_FNAME
        new_dict[(item['Dname'], item['Dnumber'], item['MGR_LNAME'], item['MGR_FNAME'])] = [{'EMP_LNAME': item['EMP_LNAME'], 'EMP_FNAME': item['EMP_FNAME'], 'Salary': item['Salary']}]

# pprint prints the data in a pretty format
#pprint(new_dict)

# create a list
new_list = []
for k, v in new_dict.items(): # keep appending dictionaries to the new list
    new_list.append({'Dname': k[0], 'Dnumber': k[1], 'MGR_LNAME': k[2], 'MGR_FNAME': k[3], 'Employees':list(v)})

pprint(new_list)

# convert a Python object into a JSON string using the dumps() method
dictionary = json.dumps(new_list)
pprint(dictionary)

print('Sending to MongoDB')
# inserts each document in the list into the collection using the insert_many()
results = departments_emps.insert_many(new_list)
# print list of _ids of the inserted documents
print(results.inserted_ids)
# results in False if there is an invalid operation
print(results.acknowledged)

# cleanup client resources and disconnect from MongoDB
client.close()