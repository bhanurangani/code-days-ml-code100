import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']

mycol = mydb["customers"]