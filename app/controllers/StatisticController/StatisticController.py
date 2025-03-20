from app.controllers.CRUDController import CRUDController
from app.models import Statistics

class StatisticController(CRUDController):
    model = Statistics

    @classmethod
    def create(cls, **kwargs):
        return super().create(**kwargs)
    
    @classmethod
    def get_all(cls):
        return super().get_all()
    
    @classmethod
    def get_one(cls, _id):
        return super().get_one(_id)
    
    @classmethod
    def get_filter_by_user(cls, user_id):
        return super().get_filter_by_user(user_id)
    
    @classmethod
    def get_filter_by(cls, **kwargs):
        return super().get_filter_by(**kwargs)
    
    @classmethod
    def update(cls, user_id, **kwargs):
        return super().update(user_id, **kwargs)
    
    @classmethod
    def delete(cls, user_id):
        return super().delete(user_id)
    
