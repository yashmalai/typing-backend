from flask import jsonify
from app.extension import db

class CRUDController:
    model = None

    @classmethod
    def create(cls, **kwargs): # cls относится к бд
        instance = cls.model(**kwargs) # Создание модели
        db.session.add(instance)
        db.session.commit()
        return jsonify({"message": "Created successfully", "id": instance.id}), 201
    
    @classmethod
    def get_all(cls): 
        instances = cls.model.query.all() 
        return jsonify([instance.to_dict() for instance in instances]), 200
    
    @classmethod
    def get_one(cls, _id): 
        instance = cls.model.query.get_or_404(_id) 
        return jsonify(instance.to_dict()), 200
    
    @classmethod
    def get_filter_by(cls, **kwargs):
        conditions = []
        
        for key, value in kwargs.items():
            if '__' in key:
                field_name, operator = key.split('__', 1)
            else:
                field_name = key
                operator = 'eq'
            
            if not hasattr(cls.model, field_name):
                continue
            
            field = getattr(cls.model, field_name)
            
            if operator == 'gt':
                conditions.append(field > value)
            elif operator == 'lt':
                conditions.append(field < value)
            elif operator == 'gte':
                conditions.append(field >= value)
            elif operator == 'lte':
                conditions.append(field <= value)
            elif operator == 'ne':
                conditions.append(field != value)
            elif operator == 'eq':
                conditions.append(field == value)
        
        instances = cls.model.query.filter(*conditions).all()
        return jsonify([instance.to_dict() for instance in instances]), 200

    @classmethod
    def get_filter_by_user(cls, _id):
        instances = cls.model.query.filter_by(user_id =_id)
        return jsonify([instance.to_dict() for instance in instances]), 200
    
    @classmethod
    def update(cls,_id, **kwargs):
        instance = cls.model.query.get_or_404(_id)
        for key, value in kwargs.items():
            setattr(instance, key, value)  # setattr нужен чтобы на выходе было instance.key = value
        db.session.commit()
        return jsonify({'message': 'Updated successfully'}), 200
    
    @classmethod
    def delete(cls, _id):
        instance = cls.model.query.get_or_404(_id)
        db.session.delete(instance)
        db.session.commit()
        return jsonify({"message": "Deleted successfully"}), 200
    
    

