from sayhello import db
from datetime import datetime


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    create_time = db.Column(db.DateTime, default=datetime.now, index=True)
    pass
