# app/main/controllers.py
from flask import Blueprint, jsonify, request, abort
from sqlalchemy import exc
from app.models import Tweet, User
from app.schemas import tweets_schema, tweet_schema
from app.schemas import users_schema, users_schema
from app import db

main = Blueprint(
    'main',
    __name__,
    url_prefix='/api/v1/',
    )

@main.errorhandler(404)
def page_not_found(e):
    response = {
        'url': request.url,
        'status': 404,
        'message': 'not found'
    }
    return jsonify(response), 404

@main.errorhandler(500)
def error_5xx(e):
    response = {
        'url': request.url,
        'status': 500,
        'message': f'{e}'
    }
    return jsonify(response), 404

@main.route('/tweets', methods=['GET'])
def get_tweets():
    tweets = db.session.query(Tweet).all() # SQLAlchemy request => 'SELECT * FROM tweets'
    return tweets_schema.jsonify(tweets)

@main.route('/tweets/<int:tweet_id>', methods=['GET'])
def get_tweet(tweet_id: int):
    return tweet_schema.jsonify(
        db.session.query(Tweet).get_or_404(tweet_id)
    )

@main.route('/tweets', methods=['POST'])
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

@main.route('/users', methods=['GET'])
def get_users():
    users = db.session.query(User).all() # SQLAlchemy request => 'SELECT * FROM tweets'
    return users_schema.jsonify(users)

@main.route('/users', methods=['POST'])
def create_user():
    requested_object = request.get_json()
    user = User()
    try:
        for attr in ['username']:
            setattr(user, attr, requested_object[attr])
    except KeyError:
        return '', 400

    db.session.add(user)
    try:
        db.session.commit()
    except exc.SQLAlchemyError as exception:
        abort(500, exception)

    return '', 204

@main.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):
    user = db.session.query(User).get_or_404(user_id)

    db.session.delete(user) # SQLAlchemy request => 'SELECT * FROM products'
    try:
        db.session.commit()
    except exc.SQLAlchemyError as exception:
        abort(500, exception)

    return '', 204