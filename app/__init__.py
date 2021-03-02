from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user_1:user123@localhost:5432/quiz_api"

db = SQLAlchemy(app)

from app.survey_crud.urls import initialize_routes
initialize_routes(api)

@app.route('/')
def index():
    return "<h1>Welcome</h1>"