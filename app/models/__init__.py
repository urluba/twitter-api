

from app import db, admin
from flask_admin.contrib.sqla import ModelView
from .user import User
from .tweet import Tweet

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Tweet, db.session))
