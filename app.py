import os

from flask import Flask, jsonify
from flask_migrate import Migrate

from models import db


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    db.init_app(app)
    Migrate(app, db, compare_type=True)

    @app.route("/")
    def hello_world():
        return jsonify({"text": "Hello, World!"})

    return app


app = create_app()
