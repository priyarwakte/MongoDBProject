
from pymongo import MongoClient

mongo = MongoClient('localhost', 27017)

proj_db = mongo.MongoProject.project
dept_db = mongo.MongoProject.department
dept_dt = mongo.MongoProject.dept_dt
emp_db = mongo.MongoProject.employee
wkson_db = mongo.MongoProject.works_on

dept_db = dept_db.find().sort("Dname")

def getMgrLName(ssn):
    data = emp_db.find_one({'Ssn': ssn})
    return data['Lname']

def getMgrFName(ssn):
    data = emp_db.find_one({'Ssn': ssn})
    return data['Fname']


def main():
    for dt in dept_db:
        lName = getMgrLName(dt['Mgr_ssn'])

        fName = getMgrFName(dt['Mgr_ssn'])

        empList = []

        for empdata in emp_db.find({}):
            if (empdata['Dno'] == dt['Dnumber']):
                empDict = {}
                empDict['EMP_LNAME'] = empdata['Lname']
                empDict['EMP_FNAME'] = empdata['Fname']
                empDict['SALARY'] = empdata['Salary']

                empList.append(empDict)

        try:
            dept_dt.insert_one({
                'DNAME': dt['Dname'],
                'DNUMBER': dt['Dnumber'],
                'MGR_LNAME': lName,
                'MGR_FNAME': fName,
                'EMPLOYEES': empList
            })

        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
