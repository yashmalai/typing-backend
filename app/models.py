from app.extension import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(70), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    user_stat = db.relationship('Statistics', backref='users', cascade="all,delete")

    def to_dict(self):
        return {
            "id": self.id,
            "login": self.login,
            "password": self.password,
            "created_at": datetime.strftime(self.created_at, "%d-%m-%Y"),
            "updated_at": datetime.strftime(self.updated_at, "%d-%m-%Y")
        }

class Statistics(db.Model):
    __tablename__ = 'statistics'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    time = db.Column(db.String(50), nullable=False)
    errors = db.Column(db.Integer, nullable=False)
    accuracy = db.Column(db.Integer, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "text": self.text,
            "accuracy": self.accuracy,
            "created_at": datetime.strftime(self.created_at, "%d-%m-%Y"),
            "updated_at": datetime.strftime(self.updated_at, "%d-%m-%Y")
        }