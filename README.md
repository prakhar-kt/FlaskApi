# FlaskApi
A Flask Rest API deployed on Heroku

#### Installation

pip3 install flask-restful
pip3 install flask-SQLAlchemy


#### Description 

The API exposes endpoints to fetch , update, create and delete movies from two database tables :
'directors' and 'movies'. 

The 'directors' table has columns 'Name' and 'Id'

The 'movies' table has columns 'name' 'year' (year of release) and 'ratings'


#### Endpoints 

READ:

GET movies list - {{url}}/movies

GET directors list - {{url}}/directors

GET movie by name - {{url}}/movie/<name>

GET director by name - {{url}}/director/<name>

CREATE:

POST movie - {{url}}/movie/<name>

POST director - {{url}}/movie/<name>

UPDATE:

PUT movie - {{url}}/movie/<name>

DELETE:

DELETE director - {{url}}/director/<name>

DELETE movie - {{url}}/movie/<name>

url : 
"https://flask-movies-rest-api.herokuapp.com"


