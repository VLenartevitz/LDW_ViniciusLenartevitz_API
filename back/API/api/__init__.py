from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)

app.config["MONGO_URI"] = 'mongodb://localhost:27017/apilivros'

api = Api(app)
mongo = PyMongo(app)
ma = Marshmallow(app)
CORS(app)

from .views import games_views