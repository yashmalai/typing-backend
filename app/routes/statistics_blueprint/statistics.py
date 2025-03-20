from flask import Blueprint, request, jsonify
from app.controllers.StatisticController import StatisticController


statistic = Blueprint("statistic_bp", __name__)

@statistic.route("/", methods=["POST"])
def create_stat():
    data = request.json
    return StatisticController.create(**data)

@statistic.route("/", methods=["GET"])
def get_all_stats():
    return StatisticController.get_all()

@statistic.route("/<int:user_id>", methods=["GET"])
def get_one_stat(user_id):
    return StatisticController.get_one(user_id)

@statistic.route("/filtered", methods=["GET"])
def get_filtered_stats():
    filters = {}
    for key, value in request.args.items():
        filters[key] = value
    return StatisticController.get_filter_by(**filters)

@statistic.route("/user/<int:user_id>", methods=["GET"])
def get_user_stats(user_id):
    return StatisticController.get_filter_by_user(user_id)

@statistic.route("/<int:user_id>", methods=["PATCH"])
def update_stat(user_id):
    data = request.json
    return StatisticController.update(user_id, **data)

@statistic.route("/<int:user_id>", methods=["DELETE"])
def delete_stat(user_id):
    return StatisticController.delete(user_id)