import os
import pymongo

client = pymongo.MongoClient("mongodb+srv://faizan:faizan@cluster0-qbjyw.mongodb.net/test?retryWrites=true&w=majority")
# print(os.environ['CHANGE_STREAM_DB'])
print(client.changestream.collection.insert_one({"hello": "world"}).inserted_id)
client.changestream.collection.update_one({"_id": 1}, {"$set": {"hello": "mars"}})
client.changestream.collection.replace_one({"_id": 1} , {"bye": "world"})
client.changestream.collection.delete_one({"_id": 1})
client.changestream.collection.drop()