from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "message": "Backend is running!",
        "application": "Book Store",
        "status": "success"
    })

@app.route("/api/books")
def books():
    return jsonify([
        {
            "id": 1,
            "title": "The Alchemist",
            "author": "Paulo Coelho"
        },
        {
            "id": 2,
            "title": "Atomic Habits",
            "author": "James Clear"
        },
        {
            "id": 3,
            "title": "The Hobbit",
            "author": "J.R.R. Tolkien"
        }
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)