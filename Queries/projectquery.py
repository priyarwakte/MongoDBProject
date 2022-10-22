

from pymongo import MongoClient

mongo = MongoClient('localhost', 27017)

db = mongo.MongoProject

def proj_rec(projName):
    print("\n Employee in Middleware project: " + projName)
    output = db.project_data.find_one({'PNAME': projName})
    print(output)




proj_rec('Middleware')
