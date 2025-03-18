from app.routes.controller import game

def register_blueprints(app):
    app.register_blueprint(game, url_prefix="")
