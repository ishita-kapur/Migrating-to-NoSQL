## Migrating-to-NoSQL

### Description

Migrating from SQL (Relational) database to NoSQL database.

### Steps to Execute

#### Bring up MongoDb

1.  Install MongoDB.
2.  Create a folder ‘data’ in C drive. Within the folder just created create two folders ‘db’ and ‘log’.
3.  Modify the dbpath and log path variables in the ‘mongod.cfg’ file. The configuration file can be found in the bin folder of MongoDB. Modify as follows: <br />
      dbpath <br />
            `dbpath: C:\data\db` <br />
      log path <br />
            `path: C:\data\log\mongo.log` <br />
4.  To start the MongoDB server, open command-prompt and navigate to the bin folder where MongoDB is installed. <br />
          `cd <mongo shell installation dir>` <br />
          `cd C:\Program Files\MongoDB\Server\4.4\bin` <br />
    Enter the following command in the command prompt terminal. <br />
          `mongod <br />
5.  To start the MongoDB client, open another command-prompt window without closing the previous one and navigate to the bin folder where MongoDB is installed. <br />
          `cd C:\Program Files\MongoDB\Server\4.4\bin` <br />
    Enter the following command in the opened command prompt terminal. <br />
          `mongo` <br />
    This connects to a MongoDB instance running on localhost with default port 27017
6.  To test if MongoDB is up and running type ‘db’ in the client terminal and press enter. This displays the current database name.

#### Execute Source Codes

1.  Create database and tables in MySQL database using the CREATE statements in the ‘create_statements.sql’ file. To insert values into MySQL execute the following command from the command-prompt: <br />
      `python insert_values.py`
2.  To convert convert tabular query results into nested object (document) structure (JSON) execute the following command from the command prompt: <br />
      i.  PROJECTS document collection <br />
            `python projects_data.py` <br />
      ii. EMPLOYEES document collection <br />
            `python employees_data.py` <br />
      iii.DEPARTMENT document collection <br />
            `python departments_data.py` <br />
     <br />
     <br />
     For XML, <br />
     execute `python projects_data_XML.py` and `python employees_data_XML.py`. <br />
     The source code when executed writes the XML data (output) to respective file ‘Projects.XML’ and ‘Employees.XML’.

#### Execute MongoDB queries

Switch the database to the created database in the mongo shell by using the following command. <br />
  `use company_db`

Type the queries into the mongo shell. <br />
e.g. `db.projects.find( { Pnumber: 22, "Employees.Lname": "Geller" } ) `
