from flask import Blueprint, request, jsonify


game = Blueprint("game_bp", __name__)

@game.route("/", methods=["POST"])
def save_statistic():
    data = request.json