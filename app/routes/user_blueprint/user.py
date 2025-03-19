from flask import Blueprint, request, jsonify
from app.controllers.UserController import UserController


user = Blueprint("game_bp", __name__)

@user.route("/", methods=["POST"])
def create_user():
    data = request.json
    return UserController.create(**data)

@user.route("/", methods=["GET"])
def get_all_users():
    return UserController.get_all()

@user.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return UserController.get_one(user_id)

@user.route("/<int:user_id>", methods=["PATCH"])
def update_user(user_id):
    data = request.json
    return UserController.update(user_id, **data)

@user.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return UserController.delete(user_id)