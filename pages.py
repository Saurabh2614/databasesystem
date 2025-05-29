from flask import jsonify, request
from app import db, app
import models
from models import Friend


# Get all friends
@app.route('/api/friends', methods=['GET'])
def get_friends():
    friends = Friend.query.all()
    return jsonify([friend.to_json() for friend in friends]), 200
