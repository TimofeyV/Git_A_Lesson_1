from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(80), unique = True, nullable = False)
    secondname = db.Column(db.String(80), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    password = db.Column(db.String)


    def __repr__(self) -> str:
        return f'User {self.firstname}, {self.email}, {self.password}'
