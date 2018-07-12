import logging
from .models import Tweet

class TweetRepository:
    ''' Tweets repo '''
    tweets = list()

    def __init__(self, logger=None):
        if logger:
            self.logger = logger
        else:
            self.logger = logging.getLogger(__name__)

    def add(self, tweet: Tweet) -> dict:
        ''' Add a tweet into the repo '''
        tweet.id = len(self.tweets)+1
        self.tweets.append(tweet)

        self.logger.debug(
            'Added new tweet "%s" (id "%s")',
            tweet,
            tweet.id
        )
        return tweet.id

    def get(self, tweet_id: int) -> Tweet:
        ''' Return a saved tweet from its index '''

        tweet = self.tweets[tweet_id - 1]
        self.logger.debug('Tweet "%s" is "%s"', tweet_id, tweet)

        return tweet

