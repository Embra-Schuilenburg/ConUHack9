from pymongo import MongoClient, collection
import streamlit as st
import csv
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

def getSingleArchetypeOverallData(archetype):
    archetypeQuery = {"player": archetype}
    data = overallCollection.find(archetypeQuery, {"_id": 0, "archetype": 0})
    for data in data:
        return(data.get("WR"), data.get("sampleSize"), data.get("confidence"))

with open('Data/statsCleaned2.csv', newline='\n') as csvfile:
    # data is read from the relative CSV containing match data, first row of the list contains column headers.
    # The 0th element of the row-0 is empty to respect that the 0th column stores the deck archetypes players can
    # select from. NOTE: There are more user selection options (120) than meta options (32)
    data = list(csv.reader(csvfile))

# populates Matchups, DO NOT UNCOMMENT or delete
# dataBase = client["MTGVersus"]
# matchupsCollection = mydb["Matchups"]
# i = 1
# j = 2
# while j <= len(data[1]):
#      while i < len(data):
#         post = {"player": data[i][0], "opp": data[0][j], "confidence": data[i][1], "WR": data[i + 1][1], "sampleSize": data[i + 2][1]}
#         x = matchupsCollection.insert_one(post)
#         i = i + 3
#     j = j + 1

# populates overall, do not uncomment!
mydb = client["MTGVersus"]
overallCollection = mydb["Overall"]
i = 1
while i < len(data) - 417:
    post = {"player": data[i][0], "confidence": data[i][1], "WR": data[i + 1][1], "sampleSize": data[i + 2][1]}
    x = overallCollection.insert_one(post)
    i = i + 3