from db import db


class MovieModel(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    year = db.Column(db.Integer)
    # ratings = db.Column(db.Float(precision=1))

    def __init__(self,name,year):
        
        
        self.name = name
        self.year = year
        # self.ratings = ratings

    

    def json(self):
        return {'name': self.name, 'year': self.year}

    @classmethod
    def find_movie_by_name(cls,name): 
        
       return cls.query.filter_by(name=name).first() # SELECT * FROM movies WHERE name=name LIMIT 1

    
    def save_to_db(self):

        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):

        db.session.delete(self)
        db.session.commit()
        