# app/main/controllers.py
from flask import Blueprint, jsonify, request
from app.models import Tweet
from app.schemas import tweets_schema, tweet_schema
from app import db

main = Blueprint('main', __name__)

@main.errorhandler(404)
def page_not_found(e):
    response = {
        'url': request.url,
        'status': 404,
        'message': 'not found'
    }
    return jsonify(response), 404

@main.route('/')
def home():
    return "Hello from a Blueprint!"

@main.route('/tweets', methods=['GET'])
@main.route('/tweets/', methods=['GET'])
def get_tweets():
    tweets = db.session.query(Tweet).all() # SQLAlchemy request => 'SELECT * FROM tweets'
    return tweets_schema.jsonify(tweets)

@main.route('/tweets/<int:tweet_id>', methods=['GET'])
def get_tweet(tweet_id: int):
    return tweet_schema.jsonify(
        db.session.query(Tweet).get_or_404(tweet_id)
    )

@main.route('/tweets', methods=['POST'])
@main.route('/tweets/', methods=['POST'])
def create_tweet():
    requested_object = request.get_json()
    tweet = Tweet()
    try:
        for attr in ['text']:
            setattr(tweet, attr, requested_object[attr])
    except KeyError:
        return '', 400

    db.session.add(tweet)
    db.session.commit()

    return tweet_schema.jsonify(tweet)

@main.route('/tweets/<int:tweet_id>', methods=['DELETE'])
def delete_tweet(tweet_id: int):
    tweet = db.session.query(Tweet).get_or_404(tweet_id)

    db.session.delete(tweet) # SQLAlchemy request => 'SELECT * FROM products'
    db.session.commit()

    return '', 204

@main.route('/tweets/<int:tweet_id>', methods=['PATCH'])
def update_tweet(tweet_id: int):
    requested_object = request.get_json()
    tweet = db.session.query(Tweet).get_or_404(tweet_id)

    try:
        for attr in ['text']:
            setattr(tweet, attr, requested_object[attr])
    except KeyError:
        pass

    db.session.commit()

    return '', 204
