from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["movieDB"]
movies_collection = db["movies"]

# Fetch all movies
movies = list(movies_collection.find({}, {"_id": 0}))  # Exclude `_id` for readability

if movies:
    print("✅ Movies found in the database:")
    for movie in movies:
        print(movie)
else:
    print("❌ No movies found in the database!")
