from app import db

#id, username, password

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)