# tests/test_models.py
from unittest import TestCase
from app.models import Tweet  # We will code our `Tweet` class in `app/models.py`

class TestTweet(TestCase):
    def test_instance_variables(self):
        tweet = Tweet("my first tweet")
        self.assertEqual(tweet.text, "my first tweet")
        self.assertIsNotNone(tweet.created_at)
        self.assertIsNone(tweet.id)
