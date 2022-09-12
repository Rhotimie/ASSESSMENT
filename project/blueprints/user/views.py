from flask import Blueprint
from flask_restful import Api
from project.blueprints.user.resources import User


user = Blueprint(
    "user", 
    __name__
)

api = Api(user)


api.add_resource(User, "", endpoint="user")
