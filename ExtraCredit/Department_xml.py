
from pymongo import MongoClient
import xml.etree.ElementTree as ET

mongo = MongoClient('localhost', 27017)

root = ET.Element("DEPARTMENT")

proj_db = mongo.MongoProject.project
dept_db = mongo.MongoProject.department
dept_dt = mongo.MongoProject.dept_dt
emp_db = mongo.MongoProject.employee
wkson_db = mongo.MongoProject.works_on

dept_db = dept_db.find().sort("Dname")

def getMgrLName(ssn):
    dt = emp_db.find_one({'Ssn': ssn})
    return dt['Lname']

def getMgrFName(ssn):
    dt = emp_db.find_one({'Ssn': ssn})
    return dt['Fname']

def main():

    for dt in dept_db:

        departmentEle = ET.SubElement(root,"DEPARTMENT")

        lName = getMgrLName(dt['Mgr_ssn'])

        fName = getMgrFName(dt['Mgr_ssn'])

        ET.SubElement(departmentEle, "DNAME").text = dt['Dname']
        ET.SubElement(departmentEle, "DNUMBER").text = str(dt['Dnumber'])
        ET.SubElement(departmentEle, "MGR_LNAME").text = lName
        ET.SubElement(departmentEle, "MGR_FNAME").text = fName

        for empdt in emp_db.find({}):
            if(empdt['Dno'] == dt['Dnumber']):

                empEle = ET.SubElement(departmentEle,"EMPLOYEE")

                ET.SubElement(empEle, 'EMP_LNAME').text = empdt['Lname']
                ET.SubElement(empEle, 'EMP_FNAME').text = empdt['Fname']
                ET.SubElement(empEle, 'SALARY').text = str(empdt['Salary'])

    tree = ET.ElementTree(root)

    #write the final tree to xml file
    tree.write('Proj2_department.xml')


if __name__ == '__main__':
    main() 
    
