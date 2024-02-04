from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://username:password@localhost/dbname')
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

@app.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    users = User.query.all()
    response = jsonify([user.to_dict() for user in users])
    return response

if __name__ == '__main__':
    app.run(debug=True)

