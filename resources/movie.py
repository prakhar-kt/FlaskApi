

from flask_restful import Resource, reqparse


from models.movie import MovieModel




class Movie(Resource):

    parser = reqparse.RequestParser() #create a parser object 
    # add the arguments to the parser object which will define what fields to look for in the request.
    parser.add_argument('year',
    type=int,
    required=True,
    help="This field cannot be left blank")
    parser.add_argument('ratings',
    type=float,
    )
    parser.add_argument('director_id',
    type=int
    )
    
    # Define a classmethod for finding a movie by name in the database
    
    
    
    def get(self,name):
        
        movie = MovieModel.find_movie_by_name(name) # call the class function

        if movie: 
            return movie.json() # if the movie exists return the movie 
        return {'message': 'Movie not found'}, 404  # else return Movie not found 

    def post(self,name):

        if MovieModel.find_movie_by_name(name): # if movie already exists , we dont have to add it again
            return {"message": "An item with name {} already exists"}, 400

        # else we parse the request using the parser object of the class
        
        data = Movie.parser.parse_args() 
        movie = MovieModel(name, **data)
        
        try:
            movie.save_to_db()
        except:
            return {"message" : "An error occured inserting the movie"}, 500 # internal server error


        return movie.json(), 201
    
    def delete(self,name):

        movie = MovieModel.find_movie_by_name(name)

        if movie:
            movie.delete_from_db()
        
        return {"message" : "Item deleted"}

    def put(self,name):
        data = Movie.parser.parse_args()
        

        movie = MovieModel.find_movie_by_name(name)

        if movie:
            movie.year = data['year']
            movie.ratings = data['ratings']
            # movie.rating = movie['ratings']
        else:
            movie = MovieModel(name, **data)

        movie.save_to_db()
        
        return movie.json()
      
        
        

class MovieList(Resource):
    
    def get(self):
        return {'movies' : [movie.json() for movie in MovieModel.query.all()]}
        
