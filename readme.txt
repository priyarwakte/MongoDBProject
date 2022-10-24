
How to run the code:
Install Mongo Db
Enter Mongo Commands
Switch to Project  Database
Import csv files into MongoDB with creating collections
mongoimport --db <MongoProject> --collection <collection name> --type csv --headerline --file <csv file name> 
Navigate to the folder containing python files
Required Packages : pymongo
pip install pymongo
To run the python code in command prompt, type the following command:
    Project.py
    Employee.py
    Department.py
    
JSON_files:
Export using below command:
mongoexport -d <db name> -c <collection name> > <JSON file name>
project.json -JSON file for project as the root 
employee.json -JSON file for employee as the root
department.json -JSON file for department as the root

Sample Query in MOngoDb CLI
db.dept_dt.findOne({'Dname':'Networking'})

Extra_Credit:
Python File for Generating XML file with Department as the root - Department_xml.py
XML file with department as root - Proj2_department.xml 

NOTE: If there is any discrepancy, there are more specific instructions in the reports.
















