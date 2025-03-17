from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["movieDB"]
movies_collection = db["movies"]

# Movie document
movie = {
    "title": "Titanic",
    "genre": ["Romance", "Drama"],
    "similar": ["The Notebook", "A Walk to Remember", "Romeo + Juliet"]
}

# Insert into MongoDB
movies_collection.insert_one(movie)
print("Titanic movie inserted successfully!")
