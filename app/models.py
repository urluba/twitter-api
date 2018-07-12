
from datetime import datetime
from app import db

class Tweet(db.Model):
    __tablename__ = "tweets"

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    text = db.Column(db.Text())
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    def __str__(self):
        return '<id {}>'.format(self.id)
