from app.routes.user_blueprint.user import user
from app.routes.statistics_blueprint import statistic

def register_blueprints(app):
    app.register_blueprint(user, url_prefix="/")
    app.register_blueprint(statistic, url_prefix="/stat")
