# tests/test_repositories.py
from unittest import TestCase
from app.models import Tweet
from app.repositories import TweetRepository


class TestTweet(TestCase):
    def test_tweet_push(self):
        my_repo = TweetRepository()
        tweet = Tweet("my first tweet")

        tweet_id = my_repo.add(tweet)

        self.assertEquals(
            my_repo.get(tweet_id).text,
            tweet.text
        )

    def test_get_unkown_tweet(self):
        my_repo = TweetRepository()

        self.assertRaises(IndexError, my_repo.get, 666)
