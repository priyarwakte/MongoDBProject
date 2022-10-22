
from pymongo import MongoClient

mongo = MongoClient('localhost', 27017)

proj_db = mongo.MongoProject.project
dept_db = mongo.MongoProject.department
emp_dt = mongo.MongoProject.emp_dt
emp_db = mongo.MongoProject.employee
wkson_db = mongo.MongoProject.works_on

emp_db = emp_db.find().sort("Lname")

def getDept(dept_no):
    dept = dept_db.find_one({'Dnumber': dept_no})
    print(dept)
    return dept['Dname']

def getProjList(empSSN):
    projList = []
    for dt in wkson_db.find({'Essn': empSSN}):
        projList.append(dt['Pno'])

    return projList


def main():

    for dt in emp_db:
        deptName = getDept(dt['Dno'])

        projList = getProjList(dt['Ssn'])

        fList = []

        for projectNum in projList:
            projdt = proj_db.find_one({'Pnumber': projectNum})
            hrs_dt = wkson_db.find_one({'Pno': projectNum, 'Essn': dt['Ssn']})
            projdict = {}
            projdict['PNAME'] = projdt['Pname']
            projdict['PNUMBER'] = projdt['Pnumber']
            projdict['HOURS'] = hrs_dt['Hours']

            fList.append(projdict)

        try:
            emp_dt.insert_one({
                'EMP_LNAME': dt['Lname'],
                'EMP_FNAME': dt['Fname'],
                'DNAME': deptName,
                'PROJECTS': fList

            })

        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
