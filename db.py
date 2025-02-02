import pathlib

from pymongo import MongoClient
import os

# MongoDB connection string (replace with your actual connection string)

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

credential_file.close()
#hello
