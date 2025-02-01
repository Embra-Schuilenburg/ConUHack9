from pymongo import MongoClient

# MongoDB connection string (replace with your actual connection string)
MONGO_URI = "mongodb://localhost:27017"  # For local MongoDB
# MONGO_URI = "mongodb+srv://your_user:password@cluster.mongodb.net/mydatabase"  # For Atlas

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["mtg_database"]  # Database name
collection = db["cards"]  # Collection name

def save_card(card_data):
    """Save card data to MongoDB."""
    collection.insert_one(card_data)

def get_all_cards():
    """Retrieve all saved cards."""
    return list(collection.find({}, {"_id": 0}))  # Exclude MongoDB's `_id` field



#hello