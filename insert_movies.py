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
         {"title": "A Star is Born", "image": "https://image.tmdb.org/t/p/w500/wrFpXMNBRj2PBiN4Z5kix51XaIZ.jpg"},
         {"title": "500 Days of Summer", "image": "https://image.tmdb.org/t/p/w500/qXAuQ9hF30sQRsXf40OfRVl0MJZ.jpg"}
     ]},
     {"title": "Kabir Singh", "genre": "Romance & drama", "image":"https://image.tmdb.org/t/p/w500/g0bIMJRQyibCEaGy8V48VviFVKM.jpg",
     "similar": [
         {"title": "Arjun Reddy", "image": "https://image.tmdb.org/t/p/w500/u9yryEQRGJYobvtneoyeIEhuCUj.jpg"},
         {"title": "Sandeep Aur Pinky Faraar", "image": "https://image.tmdb.org/t/p/w500/kxKqf6U7fmVwtFzzvDBVItS0yAS.jpg"},
         {"title": "Raanjhanaa", "image": "https://image.tmdb.org/t/p/w500/zY9YEinXLikdxbtBZddsHGT89Bl.jpg"}
     ]},
      {"title": "Ae Dil Hai Mushkil", "genre": "Romance & drama", "image": "https://image.tmdb.org/t/p/w500/hlDOF4UhUqrYY7gqLk3Rl0Fx4ns.jpg",
     "similar": [
         {"title": "Tamasha", "image": "https://image.tmdb.org/t/p/w500/8Ktf15qGVFYQ6CdBtBgCDM96UMC.jpg"},
         {"title": "Rockstar", "image": "https://image.tmdb.org/t/p/w500/2LR5ManbBWmotbM0lYCJ1TVko9P.jpg"},
         {"title": "Lootera", "image": "https://image.tmdb.org/t/p/w500/6Yd8RbKoiD4e6AK5Dcn65Od2fe2.jpg"}
     ]},
      {"title": "Yeh Jawaani Hai Deewani", "genre": "Romance & drama", "image": "https://image.tmdb.org/t/p/w500/cNkiZqlH5TsIC16tyzyShBjbcE5.jpg",
     "similar": [
         {"title": "Zindagi Na Milegi Dobara", "image": "https://image.tmdb.org/t/p/w500/hKO9O715wYxjkQSEv47giCYcyO8.jpg"},
         {"title": "Dil Chahta Hai", "image": "https://image.tmdb.org/t/p/w500/d5yjk7hbv8AK0DR0oJUrSGHMn9A.jpg"},
         {"title": "Wake Up Sid", "image": "https://image.tmdb.org/t/p/w500/1UpgW67W6Do0xizTuE26bMQFLdL.jpg"}
     ]},
    # Action
     {"title": "Blade Runner 2049", "genre": "Sci-Fi", "image": "https://image.tmdb.org/t/p/w500/gajva2L0rPYkEWjzgFlBXCAVBE5.jpg",
     "similar": [
         {"title": "Dune", "image": "https://image.tmdb.org/t/p/w500/d5NXSklXo0qyIYkgV94XAgMIckC.jpg"},
         {"title": "Arrival", "image": "https://image.tmdb.org/t/p/w500/x2FJsf1ElAgr63Y3PNPtJrcmpoe.jpg"},
         {"title": "Ex Machina", "image": "https://image.tmdb.org/t/p/w500/dmJW8IAKHKxFNiUnoDR7JfsK7Rp.jpg"}
     ]},
    {"title": "The Dark Knight", "genre": "Action", "image": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
     "similar": [
         {"title": "Gladiator", "image": "https://image.tmdb.org/t/p/w500/w0YjBWVfu689txEXZG3xa4Aev3i.jpg"},
         {"title": "Mad Max: Fury Road", "image": "https://image.tmdb.org/t/p/w500/8tZYtuWezp8JbcsvHYO0O46tFbo.jpg"},
         {"title": "John Wick", "image": "https://image.tmdb.org/t/p/w500/TxbvYS8wsgYSpYZtQLZXnoVOIQ.jpg"}
     ]},
 {"title": "Die Hard", "genre": "Action", "image": "https://image.tmdb.org/t/p/w500/bxLSU3y1AkIHByk5T7QxpmPDZSq.jpg",
     "similar": [
         {"title": "Lethal Weapon", "image": "https://image.tmdb.org/t/p/w500/fTq4ThIP3pQTYR9eDepsbDHqdcs.jpg"},
         {"title": "Speed", "image": "https://image.tmdb.org/t/p/w500/82PkCE4R95KhHICUDF7G4Ly2z3l.jpg"},
         {"title": "Mission: Impossible", "image": "https://image.tmdb.org/t/p/w500/4AZwDa0RZLIVsOgZxlgOqNUw3U6.jpg"}
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
         {"title": "Midsommar", "image": "https://image.tmdb.org/t/p/w500/eycO6M2s38xO1888Gq2gSrXf0A6.jpg"},
         {"title": "The Babadook", "image": "https://image.tmdb.org/t/p/w500/qt3fqapeo94TfvMyld8P7gkpXLz.jpg"},
         {"title": "Get Out", "image": "https://image.tmdb.org/t/p/w500/kFByXOpdP0aZokUPC16c9oWb5uN.jpg"}
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
         {"title": "Pineapple Express", "image": "https://image.tmdb.org/t/p/w500/lj4Dbyc6wZO1a2svrvrPIjCoNFx.jpg"},
         {"title": "The Hangover", "image": "https://image.tmdb.org/t/p/w500/wTt2BoyAGhr0M00eR1ewVZyQoUq.jpg"},
         {"title": "Step Brothers", "image": "https://image.tmdb.org/t/p/w500/3PNHisCtgthCGSfiNQ7zN3wHBKa.jpg"}
     ]},
    {"title": "Dumb and Dumber", "genre": "Comedy", "image": "https://image.tmdb.org/t/p/w500/4LdpGMmFspOmTveo6lUe2dHwo1P.jpg",
     "similar": [
         {"title": "Anchorman", "image": "https://image.tmdb.org/t/p/w500/mhZIcRePT7U8viFQVjt1ZjYIsR4.jpg"},
         {"title": "Zoolander", "image": "https://image.tmdb.org/t/p/w500/1VRn5gre3doau1YzNLwPRKcjPt2.jpg"},
         {"title": "The Mask", "image": "https://image.tmdb.org/t/p/w500/xcUSk3KIflAPCy1Jp64WUfuT8nN.jpg"}
     ]}
]

# Insert movies into MongoDB
movies_collection.insert_many(movies)
print("✅ Movies inserted successfully with images for similar movies!")
movies = list(movies_collection.find({}, {"_id": 0}))  # Exclude `_id` for readability
for movie in movies:
    print(movie)