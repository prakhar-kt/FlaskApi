from flask_restful import Resource, reqparse
import sqlite3




class Movie(Resource):

    parser = reqparse.RequestParser() #create a parser object 
    # add the arguments to the parser object which will define what fields to look for in the request.
    parser.add_argument('actors',
    type=list,
    required=True,
    help="This field cannot be left blank")
    parser.add_argument('ratings',
    type=float,
    )
    
    # Define a classmethod for finding a movie by name in the database
    @classmethod
    def find_movie_by_name(self,name): 
        
        connection = sqlite3.connect('Movies.db') # establish a connection 
        cursor = connection.cursor() # start the cursor 
        
        query = "SELECT * FROM movies WHERE name = ?" # define the query
        result = cursor.execute(query,(name,)) # run the query and store the results in a variable
        row = result.fetchonen # fetch the first item since we need only the first movie with the same name
        connection.close() # close the connection

        if row:  # if row is not none , ie if the movie exists return the movie name , actors and ratings
            return {'movie': {'name':row[0], 'actors': row[1], 'ratings': row[2]}} 

    @classmethod
    def insert(self,movie):

         # connect to the database
        connection = sqlite3.connect('Movies.db')
        cursor = connection.cursor()

        # define the query for insertion into the database and execute it
        query = "INSERT INTO Movies VALUES (?,?,?)"
        cursor.execute(query,(movie['name'],movie['actors'],movie['ratings']))

        #commit the query to database and close the connections
        connection.commmit()
        connection.close()

    @classmethod
    def update(self,movie):

         # connect to the database
        connection = sqlite3.connect('Movies.db')
        cursor = connection.cursor()

        # define the query for insertion into the database and execute it
        query = "UPDATE movies SET price=?, ratings=? WHERE name=?"
        cursor.execute(query,(movie['actors'],movie['ratings'],movie['name']))

        #commit the query to database and close the connections
        connection.commmit()
        connection.close()
        
    
    def get(self,name):
        
        movie = self.find_movie_name(name) # call the class function

        if movie: 
            return movie # if the movie exists return the movie 
        return {'message': 'Movie not found'}, 404  # else return Movie not found 

    def post(self,name):

        if self.find_movie_by_name(name): # if movie already exists , we dont have to add it again
            return {"message": "An item with name {} already exists"}, 400

        # else we parse the request using the parser object of the class
        
        data = Movie.parser.parse_args() 
        movie = {'name': name, 'actors' : data['actors'], 'ratings' : data['ratings']}
        
        try:
            self.insert(movie)
        except:
            return {"message" : "An error occured inserting the movie"}, 500 # internal server error


        return movie, 201
    
    def delete(self,name):

        connection = sqlite3.connect('Movies.db')
        cursor = connection.cursor()

        query = "DELETE * FROM movies WHERE name = ?"
        cursor.execute(query,(name,))

        connection.commit()
        connection.close()
        
        return {"message" : "Item deleted"}

    def put(self,name):
        data = Movie.parser.parse_args()
        updated_movie = {'name': name, 'actors': data['actors'], 'ratings' : data['ratings']}

        movie = self.find_movie_by_name(name)

        if movie:
            try:
                self.update(movie)
            except:
                return {"message" : "Movie could not be updated"} , 500
        else:
            try:
                self.insert(movie)
            except:
                return {"message" : "Movie could not be inserted"} , 500
      
        
        

class MovieList(Resource):
    
    def get(self):

        connection = sqlite3.connect('Movies.db')
        cursor = connection.cursor()

        query = "SELECT * FROM Movies"
        result = cursor.execute(query)

        movies =[]

        for row in result:
            movies.append({'name': row[0], 'actors': row[1], 'ratings' : row[2]})

        connection.close()
        

