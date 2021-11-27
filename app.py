from flask import Flask
from flask_restful import  Api 

from resources.movies import Movie, MovieList
from db import db
app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Movie, '/movie/<string:name>')
api.add_resource(MovieList, '/movies')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)