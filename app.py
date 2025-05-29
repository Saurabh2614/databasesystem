from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friends.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

import pages

hospitabel = [{
    "id": 1,
    "name": "saurabh",
    "age": 23,
    "gender": "male"
}, {
    "id": 2,
    "name": "akadu",
    "age": 23,
    "gender": "male"
}, {
    "id": 3,
    "name": "sai",
    "age": 23,
    "gender": "male"
}, {
    "id": 4,
    "name": "sai",
    "age": 23,
    "gender": "female"
}]


@app.route('/hospitabel', methods=['GET'])
def get_hospitabel():
    return jsonify(hospitabel)


@app.route('/hospitabel/<gender>', methods=['GET'])
def get_hospitabel_by_gender(gender):
    filtered_hospitabel = [
        person for person in hospitabel if person['gender'] == gender
    ]
    return jsonify(filtered_hospitabel)


@app.route('/hospitabel/<int:id>', methods=['GET'])
def get_hospitabel_by_id(id):
    new_hospitabel = [person for person in hospitabel if person['id'] == id]
    return jsonify(new_hospitabel)


@app.route('/')
def hello_world():
    return "hello world"


# return "hello world"

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
