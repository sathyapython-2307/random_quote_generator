from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

quotes = [
    "The best way to get started is to quit talking and begin doing.",
    "Success is not in what you have, but who you are.",
    "Don’t let yesterday take up too much of today.",
    "If you can dream it, you can do it.",
    "It always seems impossible until it’s done."
]

@app.route("/")
def index():
    return render_template("index.html", title="Quote Generator")

@app.route("/api/quote")
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(debug=True)
