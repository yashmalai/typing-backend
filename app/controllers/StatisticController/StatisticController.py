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
    def get_one(cls, user_id):
        return super().get_one(user_id)
    
    @classmethod
    def update(cls, user_id, **kwargs):
        return super().update(user_id, **kwargs)
    
    @classmethod
    def delete(cls, user_id):
        return super().delete(user_id)
    
