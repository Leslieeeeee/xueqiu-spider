import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.Spider
col1 = db.xqcom
col2 = db.test1
i = 11
collection = col1.find({},{$regex:})
while i < 351178:
    text = col1.find().limit(1).skip(i)
    col2.insert(text)
    i =i + 1


