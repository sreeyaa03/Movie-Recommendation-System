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
 "description": "Cobb, a skilled thief who commits corporate espionage by infiltrating the subconscious of his targets is offered a chance to regain his old life as payment for a task considered to be impossible: ""inception"", the implantation of another person's idea into a target's subconscious.", "director":"Christopher Nolan",  # Add comma here
 "rating":"7.5/10","similar_ids": [2, 3, 4]},

    {"movie_id": 2, "title": "Interstellar", "genre": "Sci-Fi", "image": "https://image.tmdb.org/t/p/w500/nCbkOyOMTEwlEV0LtCOvCnwEONA.jpg",
     "description": "The adventures of a group of explorers who make use of a newly discovered wormhole to surpass the limitations on human space travel and conquer the vast distances involved in an interstellar voyage. ", "director":"Christopher Nolan",  # Add comma here
     "rating":"8.6/10",  # Add comma here
     "similar_ids": [1, 3, 4]},
    {"movie_id": 3, "title": "The Matrix", "genre": "Sci-Fi", "image": "https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg",
        "description": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.", "director":"Lana Wachowski, Lilly Wachowski", 
        "rating":"9/10", # Add comma here
     "similar_ids": [1, 2, 4]},
    {"movie_id": 4, "title": "Avatar", "genre": "Sci-Fi", "image": "https://image.tmdb.org/t/p/w500/kyeqWdyUXW608qlYkRqosgbbJyK.jpg",
     "description": "A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.", "director":"James Cameron",  # Add comma here
     "rating":"7.8/10",  # Add comma here
     "similar_ids": [1, 2, 3]},
    {"movie_id": 5, "title": "La La Land", "genre": "Romance", "image": "https://image.tmdb.org/t/p/w500/uDO8zWDhfWwoFdKS4fzkUJt0Rf0.jpg",
     "description": "While navigating their careers in Los Angeles, a pianist and an actress fall in love while attempting to reconcile their aspirations for the future.", "director":"Damien Chazelle",  # Add comma here
     "rating":"8/10",  # Add comma here
     "similar_ids": [6, 7, 8]},
    {"movie_id": 6, "title": "Titanic", "genre": "Romance", "image": "https://image.tmdb.org/t/p/w500/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg",
        "description": "A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.", "director":"James Cameron",  # Add comma here
     "rating":"7.8/10",  # Add comma here
     "similar_ids": [5, 7, 8]},
    {"movie_id": 7, "title": "A Star is Born", "genre": "Romance", "image": "https://image.tmdb.org/t/p/w500/wrFpXMNBRj2PBiN4Z5kix51XaIZ.jpg",
        "description": "A musician helps a young singer find fame as age and alcoholism send his own career into a downward spiral.", "director":"Bradley Cooper",  # Add comma here
     "rating":"7.7/10",  # Add comma here
     "similar_ids": [5, 6, 8]},
    {"movie_id": 8, "title": "500 Days of Summer", "genre": "Romance", "image": "https://image.tmdb.org/t/p/w500/qXAuQ9hF30sQRsXf40OfRVl0MJZ.jpg",
     "description": "Tom, greeting-card writer and hopeless romantic, is caught completely off-guard when his girlfriend, Summer, suddenly dumps him. He reflects on their 500 days together to try to figure out where their love affair went sour, and in doing so, Tom rediscovers his true passions in life.", "director":"Marc Webb",  # Add comma here
    "rating":"7.7/10",  # Add comma here
     "similar_ids": [5, 6, 7]},
    {"movie_id": 9, "title": "The Dark Knight", "genre": "Action", "image": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
     "description": "When the menace known as The Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham. The Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.", "director":"Christopher Nolan",  # Add comma here
     "rating":"9/10",  # Add comma here
     "similar_ids": [10, 11, 12]},
    {"movie_id": 10, "title": "Gladiator", "genre": "Action", "image": "https://image.tmdb.org/t/p/w500/w0YjBWVfu689txEXZG3xa4Aev3i.jpg",
     "description": "After the death of Emperor Marcus Aurelius, his devious son takes power and demotes Maximus, one of Rome's most capable generals who Marcus preferred. Eventually, Maximus is forced to become a gladiator and battle to the death against other men for the amusement of paying audiences.", "director":"Ridley Scott",  # Add comma here
     "rating":"8.5/10",  # Add comma here
     "similar_ids": [9, 11, 12]},
    {"movie_id": 11, "title": "Mad Max: Fury Road", "genre": "Action", "image": "https://image.tmdb.org/t/p/w500/8tZYtuWezp8JbcsvHYO0O46tFbo.jpg",
        "description": "An apocalyptic story set in the furthest reaches of our planet, in a stark desert landscape where humanity is broken, and most everyone is crazed fighting for the necessities of life. Within this world exist two rebels on the run who just might be able to restore order.", "director":"George Miller",  # Add
     "rating":"8.1/10",  # Add comma here
     "similar_ids": [9, 10, 12]},
    {"movie_id": 12, "title": "John Wick", "genre": "Action", "image": "https://image.tmdb.org/t/p/w500/TxbvYS8wsgYSpYZtQLZXnoVOIQ.jpg",
        "description": "Ex-hitman John Wick comes out of retirement to track down the gangsters that took everything from him.", "director":"Chad Stahelski",  # Add comma here
     "rating":"7.4/10",  # Add comma here
     "similar_ids": [9, 10, 11]},
    {"movie_id": 13, "title": "The Conjuring", "genre": "Horror", "image": "https://image.tmdb.org/t/p/w500/wVYREutTvI2tmxr6ujrHT704wGF.jpg",
     "description": "Paranormal investigators Ed and Lorraine Warren work to help a family terrorized by a dark presence in their farmhouse.", "director":"James Wan",  # Add comma here
    "rating":"7.5/10",  # Add comma here
     "similar_ids": [14, 15, 16]},
    {"movie_id": 14, "title": "A Quiet Place", "genre": "Horror", "image": "https://image.tmdb.org/t/p/w500/nAU74GmpUk7t5iklEp3bufwDq4n.jpg",
        "description": "As New York City is invaded by alien creatures who hunt by sound, a woman named Sam fights to survive with her cat.", "director":"John Krasinski",  # Add comma here
     "rating":"7.5/10",  # Add comma here
     "similar_ids": [13, 15, 16]},
    {"movie_id": 15, "title": "It", "genre": "Horror", "image": "https://image.tmdb.org/t/p/w500/9E2y5Q7WlCVNEhP5GiVTjhEhx1o.jpg",
     "description": "In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.", "director":"Andy Muschietti",  # Add comma here
     "rating":"7.3/10",  # Add comma here
     "similar_ids": [13, 14, 16]},
    {"movie_id": 16, "title": "Insidious", "genre": "Horror", "image": "https://image.tmdb.org/t/p/w500/1egpmVXuXed58TH2UOnX1nATTrf.jpg",
        "description": "A family looks to prevent evil spirits from trapping their comatose child in a realm called The Further.", "director":"James Wan",  # Add comma here
    "rating":"6.8/10",  # Add comma here
     "similar_ids": [13, 14, 15]},
    {"movie_id": 17, "title": "Forrest Gump", "genre": "Drama", "image": "https://image.tmdb.org/t/p/w500/h5J4W4veyxMXDMjeNxZI46TsHOb.jpg",
     "description": "A man with a low IQ has accomplished great things in his life and been present during significant historic events—in each case, far exceeding what anyone imagined he could do. But despite all he has achieved, his one true love eludes him.", "director":"Robert Zemeckis",  # Add comma here
    "rating":"8.8/10",  # Add comma here
     "similar_ids": [18, 19, 20]},
    {"movie_id": 18, "title": "The Shawshank Redemption", "genre": "Drama", "image": "https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg",
     "description": "Imprisoned in the 1940s for the double murder of his wife and her lover, upstanding banker Andy Dufresne begins a new life at the Shawshank prison, where he puts his accounting skills to work for an amoral warden. During his long stretch in prison, Dufresne comes to be admired by the other inmates -- including an older prisoner named Red -- for his integrity and unquenchable sense of hope.", "director":"Frank Darabont",
     "rating":"7.2/10",
     "similar_ids": [17, 19, 20]},
    {"movie_id": 19, "title": "The Godfather", "genre": "Drama", "image": "https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
     "description":"An angry comedy set in the world of really organized crime.", "director":"Paul Guay",
     "rating":"7.2/10",
     "similar_ids": [17, 18, 20]},
    {"movie_id": 20, "title": "Joker", "genre": "Drama", "image": "https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg",
     "director":"During the 1980s, a failed stand-up comedian is driven insane and turns to a life of crime and chaos in Gotham City while becoming an infamous psychopathic crime figure.", "director":"Todd Phillips",  # Add comma here
     "rating":"7.2/10",  # Add comma here
     "similar_ids": [17, 18, 19]},
    {"movie_id":21,"title": "Kabir Singh", "genre": "Romance & drama", "image":"https://image.tmdb.org/t/p/w500/g0bIMJRQyibCEaGy8V48VviFVKM.jpg",
     "description": "Kabir, a genius yet hostile medical student, falls in love with Preeti from his college. When Preeti's father spots the couple kissing, he opposes their relationship and decides to marry her off. Kabir's possessiveness and anger issues soon lead him down a path of self-destruction.", "director":"Sandeep Reddy Vanga",  # Add comma here
       "rating":"7.1/10",  # Add comma here
        "similar_ids": [22, 23, 24]},
    {"movie_id":22,"title": "Arjun Reddy", "genre": "Romance & drama", "image":"https://image.tmdb.org/t/p/w500/u9yryEQRGJYobvtneoyeIEhuCUj.jpg",
     "description": "Arjun, a genius yet hostile medical student, falls in love with Preeti from his college. When Preeti's father spots the couple kissing, he opposes their relationship and decides to marry her off.", "director":"Sandeep Reddy Vanga",  # Add comma here
       "rating":"7.5/10",  # Add comma here
        "similar_ids": [21, 23, 24]},
    {"movie_id":23,"title": "Raanjhanaa", "genre": "Romance & drama", "image":"https://image.tmdb.org/t/p/w500/zY9YEinXLikdxbtBZddsHGT89Bl.jpg",
     "description": "A small-town boy needs to break through the class divide to gain acceptance from his childhood sweetheart who is in love with big city ideals.", "director":"Aanand L. Rai",  # Add comma here
       "rating":"7.6/10",  # Add comma here
        "similar_ids": [21, 22, 24]},
    {"movie_id":24,"title": "Sandeep Aur Pinky Faraar", "genre": "Romance & drama", "image":"https://image.tmdb.org/t/p/w500/kxKqf6U7fmVwtFzzvDBVItS0yAS.jpg",
        "description":"Sandeep, a bank executive & Pinky, a suspended cop, are marked for a kill. Phones tapped, accounts blocked, they escape but escaping is not freedom.", "director":"Dibakar Banerjee",  # Add comma here
       "rating":"5.7/10",  # Add comma here
        "similar_ids": [21, 22, 23]},
    {"movie_id":25,"title": "Yeh Jawani Hai Diwani", "genre": "Romance & drama", "image":"https://image.tmdb.org/t/p/w500/cNkiZqlH5TsIC16tyzyShBjbcE5.jpg",
     "description": "Kabir and Naina bond during a trekking trip. Before Naina can express herself, Kabir leaves India to pursue his career. They meet again years later, but he still cherishes his dreams more than bonds.", "director":"Ayan Mukerji",  # Add comma here
       "rating":"7.1/10",  # Add comma here
        "similar_ids": [26, 27, 28]},
    {"movie_id":26,"title": "Wake Up Sid", "genre": "Romance & drama", "image":"https://image.tmdb.org/t/p/w500/1UpgW67W6Do0xizTuE26bMQFLdL.jpg",
        "description": "Wake Up Sid! is the story of a lazy Mumbai college student who does absolutely nothing, with a turn of events will Sid realize his potential in this world and become a success in the fast-paced life of Mumbai.", "director":"Ayan Mukerji",  # Add comma here
       "rating":"7.6/10",  # Add comma here
        "similar_ids": [25, 27, 28]},
    {"movie_id":27,"title": "Zindagi Na Milegi Dobara", "genre": "Romance & drama", "image":"https://image.tmdb.org/t/p/w500/hKO9O715wYxjkQSEv47giCYcyO8.jpg",
     "description": "Three friends decide to turn their fantasy vacation into reality after one of their number becomes engaged.", "director":"Zoya Akhtar",  # Add comma here
       "rating":"8.1/10",  # Add comma here
        "similar_ids": [25, 26, 28]},
    {"movie_id":28,"title": "Dil Chahta Hai", "genre": "Romance & drama", "image":"https://image.tmdb.org/t/p/w500/d5yjk7hbv8AK0DR0oJUrSGHMn9A.jpg",
     "description": "Three inseparable childhood friends are just out of college. Nothing comes between them - until they each fall in love, and their wildly different approaches to relationships creates tension.", "director":"Farhan Akhtar",  # Add comma here
        "rating":"8.1/10",  # Add comma here
        "similar_ids": [25, 26, 27]},
        

]

# Insert movies into MongoDB
try:
    movies_collection.insert_many(movies)
    print("✅ All movies inserted successfully!")
    
    # Retrieve and print inserted movies
    movies = list(movies_collection.find({}, {"_id": 0}))
    for movie in movies:
        print(movie)
except Exception as e:
    print(f"❌ Error inserting movies: {e}")