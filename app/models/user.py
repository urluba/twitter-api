
from datetime import datetime
from app import db
from uuid import uuid4

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(32),
        unique=True,
    )

    api_token = db.Column(
        db.Text(),
        unique=True,
        default=uuid4()
    )

    def __str__(self):
        return '<id {}>'.format(self.id)
