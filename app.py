from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return jsonify({"text": "Hello, World!"})

    return app

app = create_app()
