import os
import pymongo
from bson.json_util import dumps
from flask_socketio import emit

client = pymongo.MongoClient("mongodb+srv://faizan:faizan@cluster0-qbjyw.mongodb.net/test?retryWrites=true&w=majority")
change_stream = client.changestream.collection.watch()

for change in change_stream:
    emit('new_document_inserted', change)
    print(dumps(change))
    print('') # for readability only