from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db_uri = os.environ.get('DATABASE_URL', 'postgresql://username:password@localhost/dbname')
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)

@app.route('/')
def index():
    return jsonify({'message': 'Bienvenue sur le Backend Python'})

if __name__ == '__main__':
    app.run(debug=True)

