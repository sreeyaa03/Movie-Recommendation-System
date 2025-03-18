from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["movieDB"]
movies_collection = db["movies"]

# Clear previous movie data (optional, to avoid duplicates)
movies_collection.delete_many({})

# Define movies with unique IDs
movies = [
    {"movie_id": 1, "title": "Inception", "genre": "Sci-Fi", "image": "https://image.tmdb.org/t/p/w500/ljsZTbVsrQSqZgWeep2B1QiDKuh.jpg",
     "similar_ids": [2, 3, 4]},
    {"movie_id": 2, "title": "Interstellar", "genre": "Sci-Fi", "image": "https://image.tmdb.org/t/p/w500/nCbkOyOMTEwlEV0LtCOvCnwEONA.jpg",
     "similar_ids": [1, 3, 4]},
    {"movie_id": 3, "title": "The Matrix", "genre": "Sci-Fi", "image": "https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg",
     "similar_ids": [1, 2, 4]},
    {"movie_id": 4, "title": "Avatar", "genre": "Sci-Fi", "image": "https://image.tmdb.org/t/p/w500/kyeqWdyUXW608qlYkRqosgbbJyK.jpg",
     "similar_ids": [1, 2, 3]},
    {"movie_id": 5, "title": "La La Land", "genre": "Romance", "image": "https://image.tmdb.org/t/p/w500/uDO8zWDhfWwoFdKS4fzkUJt0Rf0.jpg",
     "similar_ids": [6, 7, 8]},
    {"movie_id": 6, "title": "Titanic", "genre": "Romance", "image": "https://image.tmdb.org/t/p/w500/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg",
     "similar_ids": [5, 7, 8]},
    {"movie_id": 7, "title": "A Star is Born", "genre": "Romance", "image": "https://image.tmdb.org/t/p/w500/wrFpXMNBRj2PBiN4Z5kix51XaIZ.jpg",
     "similar_ids": [5, 6, 8]},
    {"movie_id": 8, "title": "500 Days of Summer", "genre": "Romance", "image": "https://image.tmdb.org/t/p/w500/qXAuQ9hF30sQRsXf40OfRVl0MJZ.jpg",
     "similar_ids": [5, 6, 7]},
    {"movie_id": 9, "title": "The Dark Knight", "genre": "Action", "image": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
     "similar_ids": [10, 11, 12]},
    {"movie_id": 10, "title": "Gladiator", "genre": "Action", "image": "https://image.tmdb.org/t/p/w500/w0YjBWVfu689txEXZG3xa4Aev3i.jpg",
     "similar_ids": [9, 11, 12]},
    {"movie_id": 11, "title": "Mad Max: Fury Road", "genre": "Action", "image": "https://image.tmdb.org/t/p/w500/8tZYtuWezp8JbcsvHYO0O46tFbo.jpg",
     "similar_ids": [9, 10, 12]},
    {"movie_id": 12, "title": "John Wick", "genre": "Action", "image": "https://image.tmdb.org/t/p/w500/TxbvYS8wsgYSpYZtQLZXnoVOIQ.jpg",
     "similar_ids": [9, 10, 11]},
    {"movie_id": 13, "title": "The Conjuring", "genre": "Horror", "image": "https://image.tmdb.org/t/p/w500/3cbmY8ooSkWgF1kudL2WBnFZn2T.jpg",
     "similar_ids": [14, 15, 16]},
    {"movie_id": 14, "title": "A Quiet Place", "genre": "Horror", "image": "https://image.tmdb.org/t/p/w500/nAU74GmpUk7t5iklEp3bufwDq4n.jpg",
     "similar_ids": [13, 15, 16]},
    {"movie_id": 15, "title": "It", "genre": "Horror", "image": "https://image.tmdb.org/t/p/w500/9E2y5Q7WlCVNEhP5GiVTjhEhx1o.jpg",
     "similar_ids": [13, 14, 16]},
    {"movie_id": 16, "title": "Insidious", "genre": "Horror", "image": "https://image.tmdb.org/t/p/w500/1egpmVXuXed58TH2UOnX1nATTrf.jpg",
     "similar_ids": [13, 14, 15]},
    {"movie_id": 17, "title": "Forrest Gump", "genre": "Drama", "image": "https://image.tmdb.org/t/p/w500/h5J4W4veyxMXDMjeNxZI46TsHOb.jpg",
     "similar_ids": [18, 19, 20]},
    {"movie_id": 18, "title": "The Shawshank Redemption", "genre": "Drama", "image": "https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg",
     "similar_ids": [17, 19, 20]},
    {"movie_id": 19, "title": "The Godfather", "genre": "Drama", "image": "https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
     "similar_ids": [17, 18, 20]},
    {"movie_id": 20, "title": "Joker", "genre": "Drama", "image": "https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg",
     "similar_ids": [17, 18, 19]}
]

# Insert movies into MongoDB
movies_collection.insert_many(movies)
print("✅ All movies inserted successfully!")

# Retrieve and print inserted movies (excluding _id for readability)
movies = list(movies_collection.find({}, {"_id": 0}))
for movie in movies:
    print(movie)
