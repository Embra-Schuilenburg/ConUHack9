import certifi
from pymongo import MongoClient, collection
import os

# MongoDB connection string (replace with your actual connection string)

os.chdir('../Credentials/')
credential_file = open( os.path.join(os.getcwd(),'EngiQDB.txt'))
print(credential_file)

MONGO_URI = str(credential_file.readline())  # From your personal credential file

def get_all_archetypes():
    """Retrieve all saved cards."""
    return list(collection.find({}, {"player": 0}))  # Exclude MongoDB's `_id` field

def get_archetype(param):
    return collection.find({"player": param}) #TODO change after correct data

# Connect to MongoDB
client = MongoClient(MONGO_URI,  tlsCAFile=certifi.where())
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Access granted")
except Exception as e:
    print(e)

credential_file.close()