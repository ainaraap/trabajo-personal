from flask import Flask, request
from flask_cors import CORS


from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/dolls", methods=["GET"])
    def dolls_get():
        dolls = repositories["dolls"].get_dolls()
        return object_to_json(dolls)

    @app.route("/api/dolls/<doll_id>", methods=["GET"])
    def doll_get_by_id(doll_id):
        doll = repositories["dolls"].get_dolls_by_id(doll_id)
        return object_to_json(doll)

    @app.route("/auth/admin", methods=["POST"])
    def admin():
        body = request.json
        user = repositories["user"].get_by_id(body["user"])

        if user is None or (body["password"]) != user.password:
            return "", 401

        return user.to_dict(), 200

    return app
