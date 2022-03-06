import os
from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return jsonify({"DATABASE_URL": os.getenv('DATABASE_URL')})

    return app

app = create_app()
