from pymongo import MongoClient, collection
import streamlit as st
#import csv
#import certifi

MONGO_URI = str(st.secrets["DB_URI"])  # From Streamlit secrets file

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