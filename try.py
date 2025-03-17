from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["movieDB"]
movies_collection = db["movies"]

# Fetch all movies
movies = movies_collection.find()
for movie in movies:
    print(movie)
