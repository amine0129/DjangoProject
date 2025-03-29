from pymongo import MongoClient

client =MongoClient("mongodb://localhost:27017/")
db=client['sportclub']
subscribers =db['sub']
admins=db['admins']
