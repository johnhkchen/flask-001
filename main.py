from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Beep beep": "It's a jeep!"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
