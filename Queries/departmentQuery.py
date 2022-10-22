

from pymongo import MongoClient

mongo = MongoClient('localhost', 27017)

db = mongo.MongoProject

def dept_rec(DName):
    print("\nEmployee in Networking department: " + DName)
    output = db.department_data.find_one({'DNAME':DName})
    print(output)

dept_rec('Networking')


