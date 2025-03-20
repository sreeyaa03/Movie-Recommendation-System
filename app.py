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
    """ Recommend movies based on a given movie name. """
    movie_name = request.args.get("movie", "").strip()

    if not movie_name:
        return jsonify({"error": "Please enter a movie name"}), 400

    print(f"🔍 Searching for movie: '{movie_name}'")  # Debugging log

    # Find the movie in MongoDB (case-insensitive search, partial match)
    movie = movies_collection.find_one({"title": {"$regex": f"^{movie_name}$", "$options": "i"}})

    if not movie:
        print("❌ Movie not found in the database")
        return jsonify({"error": "Movie not found in database"}), 404

    # Get similar movie IDs
    similar_ids = movie.get("similar_ids", [])

    if not similar_ids:
        return jsonify({"error": "No recommendations found"}), 404

    # Fetch recommended movies (include title, image, and description)
    recommended_movies = list(
        movies_collection.find(
            {"movie_id": {"$in": similar_ids}},
            {"_id": 0, "title": 1, "image": 1, "description": 1, "movie_id": 1}
        )
    )

    print(f"✅ Recommended movies: {recommended_movies}")  # Debugging log

    return jsonify({"recommended": recommended_movies})


@app.route("/movie", methods=["GET"])
def get_movie():
    """ Fetch detailed information about a specific movie using movie_id. """
    movie_id = request.args.get("movie_id")

    if not movie_id or movie_id.lower() in ["undefined", "null"]:
        return jsonify({"error": "Invalid movie ID"}), 400

    try:
        movie_id = int(movie_id)  # Convert to integer
    except ValueError:
        print("⚠️ Invalid movie ID received:", movie_id)
        return jsonify({"error": "Invalid movie ID"}), 400

    movie = movies_collection.find_one({"movie_id": movie_id}, {"_id": 0})

    if not movie:
        print(f"❌ Movie with ID {movie_id} not found")
        return jsonify({"error": "Movie not found"}), 404

    print(f"✅ Movie found: {movie}")  # Debugging log

    return jsonify(movie)



if __name__ == "__main__":
    app.run(debug=True)
