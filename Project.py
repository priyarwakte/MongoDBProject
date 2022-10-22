
from pymongo import MongoClient

mongo = MongoClient('localhost', 27017)

proj_db = mongo.MongoProject.project
dept_db = mongo.MongoProject.department
proj_dt = mongo.MongoProject.proj_dt
emp_db = mongo.MongoProject.employee
wkson_db = mongo.MongoProject.works_on


proj_db = proj_db.find().sort("Pname")

def getDept(deptnum):
    dept = dept_db.find_one({'Dnumber': deptnum})
    return dept['Dname']

def getEmpSSNLst(projNum):
    ssnList = []
    for data in wkson_db.find({'Pno': projNum}):
        ssnList.append(data['Essn'])
    return ssnList

def main():

    for dt in proj_db:
        deptName = getDept(dt['Dnum'])

        ssnlist = getEmpSSNLst(dt['Pnumber'])

        empList = []

        for ssn in ssnlist:
            empdata = emp_db.find_one({'Ssn': ssn})
            hrsdt = wkson_db.find_one({'Essn': ssn, 'Pno': dt['Pnumber']})
            empdict = {}
            empdict['EMP_LNAME'] = empdata['Lname']
            empdict['EMP_FNAME'] = empdata['Fname']
            empdict['HOURS'] = hrsdt['Hours']

            empList.append(empdict)

        try:
            proj_dt.insert_one({
                'PNAME': dt['Pname'],
                'PNUMBER': dt['Pnumber'],
                'DNAME': deptName,
                'EMPLOYEES': empList

            })

        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
