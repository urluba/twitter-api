from app import ma
from app.models.user import User

class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ('id', 'username', 'api_token')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
