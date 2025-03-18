from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["movieDB"]
movies_collection = db["movies"]

# Delete existing movies (optional, to avoid duplicates)
movies_collection.delete_many({})

# Movie data with images for both movies and their similar ones
movies = [
    # Sci-Fi
    {"title": "Inception", "genre": "Sci-Fi", "image": "https://image.tmdb.org/t/p/w500/ljsZTbVsrQSqZgWeep2B1QiDKuh.jpg",
     "similar": [
         {"title": "Interstellar", "image": "https://image.tmdb.org/t/p/w500/nCbkOyOMTEwlEV0LtCOvCnwEONA.jpg"},
         {"title": "The Matrix", "image": "https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg"},
         {"title": "Avatar", "image": "https://image.tmdb.org/t/p/w500/kyeqWdyUXW608qlYkRqosgbbJyK.jpg"}
     ]},

    {"title": "Interstellar", "genre": "Sci-Fi", "image": "https://image.tmdb.org/t/p/w500/nCbkOyOMTEwlEV0LtCOvCnwEONA.jpg",
     "similar": [
         {"title": "Inception", "image": "https://image.tmdb.org/t/p/w500/ljsZTbVsrQSqZgWeep2B1QiDKuh.jpg"},
         {"title": "The Matrix", "image": "https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg"},
         {"title": "Avatar", "image": "https://image.tmdb.org/t/p/w500/kyeqWdyUXW608qlYkRqosgbbJyK.jpg"}
     ]},
  {"title": "La La Land", "genre": "Romance", "image": "https://image.tmdb.org/t/p/w500/uDO8zWDhfWwoFdKS4fzkUJt0Rf0.jpg",
     "similar": [
         {"title": "Titanic", "image": "https://image.tmdb.org/t/p/w500/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg"},
         {"title": "A Star is Born", "image": "https://image.tmdb.org/t/p/w500/7GWjV9e5I38XqIb3dx5CyvXnYdx.jpg"},
         {"title": "500 Days of Summer", "image": "https://image.tmdb.org/t/p/w500l/qXAuQ9hF30sQRsXf40OfRVl0MJZ.jpg"}
     ]},
    # Action
     {"title": "Blade Runner 2049", "genre": "Sci-Fi", "image": "https://image.tmdb.org/t/p/w500/gajva2L0rPYkEWjzgFlBXCAVBE5.jpg",
     "similar": [
         {"title": "Dune", "image": "https://image.tmdb.org/t/p/w500/d5NXSklXo0qyIYkgV94XAgMIckC.jpg"},
         {"title": "Arrival", "image": "https://image.tmdb.org/t/p/w500/x2FJsf1ElAgr63Y3PNPtJrcmpoe.jpg"},
         {"title": "Ex Machina", "image": "https://image.tmdb.org/t/p/w500/iJQIbOPm81fPEGKt5BPuZmfnA54.jpg"}
     ]},
    {"title": "The Dark Knight", "genre": "Action", "image": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
     "similar": [
         {"title": "Gladiator", "image": "https://image.tmdb.org/t/p/w500/pRn3TJHbAqCAO6U8Dw5DayVUuO0.jpg"},
         {"title": "Mad Max: Fury Road", "image": "https://image.tmdb.org/t/p/w500/8tZYtuWezp8JbcsvHYO0O46tFbo.jpg"},
         {"title": "John Wick", "image": "https://image.tmdb.org/t/p/w500/rEJxuttwQ3dM1aapHBvkcmoZyJc.jpg"}
     ]},
 {"title": "Die Hard", "genre": "Action", "image": "https://image.tmdb.org/t/p/w500/bxLSU3y1AkIHByk5T7QxpmPDZSq.jpg",
     "similar": [
         {"title": "Lethal Weapon", "image": "https://image.tmdb.org/t/p/w500/gBqJ5D1N8oZxDpNRJiyGq4U6WKO.jpg"},
         {"title": "Speed", "image": "https://image.tmdb.org/t/p/w500/rgA4jOe0txSkpbcfrA1F9U5AbIk.jpg"},
         {"title": "Mission: Impossible", "image": "https://image.tmdb.org/t/p/w500/l5phE2wlnY1Syj0yMLXx2XKcb5P.jpg"}
     ]},
    # Romance
    {"title": "Titanic", "genre": "Romance", "image": "https://image.tmdb.org/t/p/w500/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg",
     "similar": [
         {"title": "The Notebook", "image": "https://image.tmdb.org/t/p/w500/6WpJMNaJqbuPce775jGLpBWO1B0.jpg"},
         {"title": "La La Land", "image": "https://image.tmdb.org/t/p/w500/uDO8zWDhfWwoFdKS4fzkUJt0Rf0.jpg"},
         {"title": "Pride and Prejudice", "image": "https://image.tmdb.org/t/p/w500/sGjIvtVvTlWnia2zfJfHz81pZ9Q.jpg"}
     ]},

    # Horror
    {"title": "The Conjuring", "genre": "Horror", "image": "https://image.tmdb.org/t/p/w500/3cbmY8ooSkWgF1kudL2WBnFZn2T.jpg",
     "similar": [
         {"title": "A Quiet Place", "image": "https://image.tmdb.org/t/p/w500/nAU74GmpUk7t5iklEp3bufwDq4n.jpg"},
         {"title": "It", "image": "https://image.tmdb.org/t/p/w500/9E2y5Q7WlCVNEhP5GiVTjhEhx1o.jpg"},
         {"title": "Insidious", "image": "https://image.tmdb.org/t/p/w500/1egpmVXuXed58TH2UOnX1nATTrf.jpg"}
     ]},
 {"title": "Hereditary", "genre": "Horror", "image": "https://image.tmdb.org/t/p/w500/lHV8HHlhwNup2VbpiACtlKzaGIQ.jpg",
     "similar": [
         {"title": "Midsommar", "image": "https://image.tmdb.org/t/p/w500/rXMX4KJJD0z3XJU2f7KjGzggD0r.jpg"},
         {"title": "The Babadook", "image": "https://image.tmdb.org/t/p/w500/sugXJmMhwIdNCwhR1AsFh9nFikF.jpg"},
         {"title": "Get Out", "image": "https://image.tmdb.org/t/p/w500/tFXcEccSQMf3lfhfXKSU9iRBpa3.jpg"}
     ]},
    # Drama
    {"title": "Forrest Gump", "genre": "Drama", "image": "https://image.tmdb.org/t/p/w500/h5J4W4veyxMXDMjeNxZI46TsHOb.jpg",
     "similar": [
         {"title": "The Shawshank Redemption", "image": "https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg"},
         {"title": "The Godfather", "image": "https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg"},
         {"title": "Joker", "image": "https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg"}
     ]},
     {"title": "Superbad", "genre": "Comedy", "image": "https://image.tmdb.org/t/p/w500/ek8e8txUyUwdUWDKA5E3vDgfHts.jpg",
     "similar": [
         {"title": "Pineapple Express", "image": "https://image.tmdb.org/t/p/w500/g0xKypo6hEyG5GUBS3wCD7nRIpZ.jpg"},
         {"title": "The Hangover", "image": "https://image.tmdb.org/t/p/w500/k7Nl6hoK67z75E95OEiHk4rh2m3.jpg"},
         {"title": "Step Brothers", "image": "https://image.tmdb.org/t/p/w500/8fWmx5mca8zbbh0iD1L4ucjQZBV.jpg"}
     ]},
    {"title": "Dumb and Dumber", "genre": "Comedy", "image": "https://image.tmdb.org/t/p/w500/4LdpGMmFspOmTveo6lUe2dHwo1P.jpg",
     "similar": [
         {"title": "Anchorman", "image": "https://image.tmdb.org/t/p/w500/kZ4vC2vdq0YspFzHDyudlMMiYbb.jpg"},
         {"title": "Zoolander", "image": "https://image.tmdb.org/t/p/w500/9K6Hr8D6i7XtUdfjocbVG7S3oEb.jpg"},
         {"title": "The Mask", "image": "https://image.tmdb.org/t/p/w500/f4ox8bbl6IKGpRieI1l0uPsbmow.jpg"}
     ]}
]

# Insert movies into MongoDB
movies_collection.insert_many(movies)
print("✅ Movies inserted successfully with images for similar movies!")
movies = list(movies_collection.find({}, {"_id": 0}))  # Exclude `_id` for readability
for movie in movies:
    print(movie)