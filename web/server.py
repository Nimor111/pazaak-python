import os
from flask import Flask, jsonify, request

from pazaak.board import PazaakBoard
from pazaak.state import PazaakState

app = Flask(__name__)
port = int(os.getenv('PORT', 3000))


@app.route('/')
def index():
    print(request.get_json())
    return jsonify(board=[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
