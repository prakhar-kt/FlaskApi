from db import db


class DirectorModel(db.Model):
    __tablename__ = 'directors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    
    movies = db.relationship("MovieModel")

    def __init__(self,name):
        
        self.name = name
        
        
        

    

    def json(self):
        return {'name': self.name, 'movies' : [movie.json() for movie in  self.movies]}

    @classmethod
    def find_director_by_name(cls,name): 
        
       return cls.query.filter_by(name=name).first()

    
    def save_to_db(self):

        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):

        db.session.delete(self)
        db.session.commit()
        