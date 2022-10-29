from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def home():
    slack_username = "jimi"
    age = 24
    bio = "I am curious about how things work"
    return jsonify ({
        "slackUsername": slack_username,
        "backend": True,
        "age": age,
        "bio": bio
    })

if __name__ == "__main__":
    app.run()