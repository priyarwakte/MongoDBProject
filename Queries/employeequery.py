

from pymongo import MongoClient

mongo = MongoClient('localhost', 27017)

db = mongo.MongoProject

def emp_rec(fName, Lname):
    print("\nProjects Of Ahmad: " + fName + " " + Lname)
    output = db.emp_dt.find_one({'EMP_LNAME': Lname, 'EMP_FNAME':fName})
    print(output)



emp_rec('Ahmad', 'Jabbar')

