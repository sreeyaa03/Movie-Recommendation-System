from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["movieDB"]
movies_collection = db["movies"]

@app.route("/recommend", methods=["GET"])
def recommend_movie():
    movie_name = request.args.get("movie", "").strip()

    if not movie_name:
        return jsonify({"error": "Please enter a movie name"}), 400

    print(f"🔍 Searching for movie: '{movie_name}'")  # Debugging log

    # Find the movie in MongoDB (case-insensitive search)
    movie = movies_collection.find_one({"title": {"$regex": f"^{movie_name}$", "$options": "i"}})

    if not movie:
        print("❌ Movie not found in the database")
        return jsonify({"error": "Movie not found in database"}), 404

    # Get similar movie IDs
    similar_ids = movie.get("similar_ids", [])

    if not similar_ids:
        return jsonify({"error": "No recommendations found"}), 404

    # Fetch recommended movies
    recommended_movies = list(movies_collection.find({"movie_id": {"$in": similar_ids}}, {"_id": 0, "title": 1, "image": 1}))

    print(f"✅ Recommended movies: {recommended_movies}")  # Debugging log

    return jsonify({"recommended": recommended_movies})

if __name__ == "__main__":
    app.run(debug=True)
