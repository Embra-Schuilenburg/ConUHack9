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

# Old, populates Matchups, DO NOT UNCOMMENT
# mydb = client["MTGVersus"]
# mycol = mydb["Matchups"]
# i = 1
# j = 2
# while j <= len(data[1]):
#     while i < len(data):
#         post = {"player": data[i][0], "opp": data[0][j], "confidence": data[i][1], "WR": data[i + 1][1], "sampleSize": data[i + 2][1]}
#         x = mycol.insert_one(post)
#         i = i + 3
#     j = j + 1