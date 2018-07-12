from app import ma
from app.models import Tweet

class TweetSchema(ma.Schema):
    class Meta:
        model = Tweet
        fields = ('id', 'text', 'created_at')

tweet_schema = TweetSchema()
tweets_schema = TweetSchema(many=True)
