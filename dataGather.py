import pathlib

from pymongo import MongoClient
import certifi
from pymongo import MongoClient, collection
import os
import csv

os.chdir("C:\software\Pycharm\conUHacks9")

# fix later
credential_file = open("C:\software\Pycharm\Credentials\EngiQDB.txt")

MONGO_URI = str(credential_file.readline())  # From your personal credential file

# Connect to MongoDB
client = MongoClient(MONGO_URI)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Access granted")
except Exception as e:
    print(e)

mydb = client["MTGVersus"]
OverallCollection = mydb["Overall"]

def getSingleArchetypeOverallData(archetype):
    archetypeQuery = {"player": archetype}
    data = OverallCollection.find(archetypeQuery, {"_id": 0, "archetype": 0 })
    for data in data:
        return(data.get("WR"), data.get("sampleSize"), data.get("confidence"))



credential_file.close()
