from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["movieDB"]
movies_collection = db["movies"]

# Movie document
movie = {
    "title": "Inception",
    "genre": ["Sci-Fi", "Thriller"],
    "similar": ["Interstellar", "The Prestige", "Shutter Island"]
}

# Insert into MongoDB
movies_collection.insert_one(movie)
print("Movie inserted successfully!")
