from flask import Blueprint, request, jsonify
from app.controllers.StatisticController import StatisticController


statistic = Blueprint("statistic_bp", __name__)

@statistic.route("/", methods=["POST"])
def create_user():
    data = request.json
    return StatisticController.create(**data)

@statistic.route("/", methods=["GET"])
def get_all_users():
    return StatisticController.get_all()

@statistic.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return StatisticController.get_one(user_id)

@statistic.route("/<int:user_id>", methods=["PATCH"])
def update_user(user_id):
    data = request.json
    return StatisticController.update(user_id, **data)

@statistic.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return StatisticController.delete(user_id)