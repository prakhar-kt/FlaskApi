import sqlite3


class MovieModel:

    def __init__(self,_id,name,actors,ratings):
        
        self.id = _id
        self.name = name
        self.actors = actors
        self.ratings = ratings

    def find_movie_by_name(self,name):
        pass

    def json(self):
        return {'name': self.name, 'actors': self.actors, 'ratings': self.rating}

    @classmethod
    def find_movie_by_name(cls,name): 
        
        connection = sqlite3.connect('Movies.db') # establish a connection 
        cursor = connection.cursor() # start the cursor 
        
        query = "SELECT * FROM movies WHERE name = ?" # define the query
        result = cursor.execute(query,(name,)) # run the query and store the results in a variable
        row = result.fetchonen # fetch the first item since we need only the first movie with the same name
        connection.close() # close the connection

        if row:  # if row is not none , ie if the movie exists return the movie name , actors and ratings
            return cls(*row)

    
    def insert(self):

         # connect to the database
        connection = sqlite3.connect('Movies.db')
        cursor = connection.cursor()

        # define the query for insertion into the database and execute it
        query = "INSERT INTO Movies VALUES (?,?,?)"
        cursor.execute(query,(self.name,self.actors,self.ratings))

        #commit the query to database and close the connections
        connection.commmit()
        connection.close()

    
    def update(self):

         # connect to the database
        connection = sqlite3.connect('Movies.db')
        cursor = connection.cursor()

        # define the query for insertion into the database and execute it
        query = "UPDATE movies SET price=?, ratings=? WHERE name=?"
        cursor.execute(query,(self.actors,self.ratings,self.name))

        #commit the query to database and close the connections
        connection.commmit()
        connection.close()
        
