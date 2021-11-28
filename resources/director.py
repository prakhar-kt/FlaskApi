from flask_restful import Resource

from models.director import DirectorModel

class Director(Resource):

    def get(self,name):
        director  = DirectorModel.find_director_by_name(name)

        if director:
            return director.json()
        else:
            return {'message': 'Director does not exist'}, 404

    
        

    def post(self,name):
        if DirectorModel.find_director_by_name(name):
            return {'messsage': 'Director already exists'}, 400

        director = DirectorModel(name)

        try:
            director.save_to_db()
        except:
            return {'message': 'Director could not be added'}, 500
        
        return director.json(), 201

    def delete(self,name):

        director = DirectorModel.find_director_by_name(name)

        if director:
            director.delete_from_db()
            return {'message': 'Director  deleted'}
        else:
            return {'message': 'Director does not exist'} , 400

class DirectorList(Resource):
    def get(self):
        return {'directors': [director.json() for director in DirectorModel.query.all()]}

