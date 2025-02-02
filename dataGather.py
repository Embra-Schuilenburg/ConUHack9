import pathlib

from pymongo import MongoClient
import certifi
from pymongo import MongoClient, collection
import os
import csv

os.chdir("C:\software\Pycharm\conUHacks9")
with open('Data/statsCleaned.csv', newline='\n') as csvfile:
    # data is read from the relative CSV containing match data, first row of the list contains column headers.
    # The 0th element of the row-0 is empty to respect that the 0th column stores the deck archetypes players can
    # select from. NOTE: There are more user selection options (120) than meta options (32)
    data = list(csv.reader(csvfile))

os.chdir('../Credentials/')
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
mycol = mydb["Overall"]

i = 1
while i < len(data) - 417:
    post = {"player": data[i][0], "confidence": data[i][1], "WR": data[i + 1][1], "sampleSize": data[i + 2][1]}
    x = mycol.insert_one(post)
    i = i + 3


credential_file.close()
