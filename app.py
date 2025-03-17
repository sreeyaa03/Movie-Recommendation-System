from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017/")
db = client["movieDB"]
movies_collection = db["movies"]

@app.route("/recommend", methods=["GET"])
def recommend_movie():
    movie_name = request.args.get("movie")
    if not movie_name:
        return jsonify({"error": "Please enter a movie name"}), 400

    movie = movies_collection.find_one({"title": {"$regex": f"^{movie_name}$", "$options": "i"}})

    if not movie:
        return jsonify({"error": "Movie not found in database"}), 404

    recommendations = movie["similar"]
    return jsonify({"recommended": recommendations})

if __name__ == "__main__":
    app.run(debug=True)
