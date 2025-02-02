import certifi
from pymongo import MongoClient, collection
import os

# MongoDB connection string (replace with your actual connection string)

os.chdir('../Credentials/')
credential_file = open( os.path.join(os.getcwd(),'EngiQDB.txt'))
print(credential_file)

MONGO_URI = str(credential_file.readline())  # From your personal credential file



# Connect to MongoDB
client = MongoClient(MONGO_URI,  tlsCAFile=certifi.where())
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Access granted")
except Exception as e:
    print(e)

db = client["MTGVersus"]

def get_all_archetypes():
    """Retrieve all saved cards."""
    return list(collection.find({}, {"player": 0}))  # Exclude MongoDB's `_id` field

def get_archetype(param):
    return db.article.find({"$and": [{"player": "Izzet Phoenix", "sampleSize": {"$gte": 10}}]})

credential_file.close()