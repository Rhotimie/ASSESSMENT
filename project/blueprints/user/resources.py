from flask import request
from sqlalchemy import text
from flask_restful import Resource
from marshmallow import EXCLUDE
from project.blueprints.user.models import UserModel
from project.blueprints.user.schemas import UserSchema


user_schema = UserSchema(unknown=EXCLUDE)
multiple_user_schema = UserSchema(many=True)


class UsersList(Resource):
    @classmethod
    def get(cls,):
        sort_by = UserModel.sort_by(request.args.get('sort', 'created_on'),
                        request.args.get('direction', 'desc'))
        order_values = 'users.{0} {1}'.format(sort_by[0], sort_by[1])
        
        # implement caching
        
        page = int(request.args.get('page', 1))
        
        users_per_page = int(request.args.get('users_per_page', 20))
        
        page_object = UserModel.query.filter(UserModel.search(request.args.get('q', ''))) \
            .order_by(text(order_values)) \
            .paginate(page, users_per_page,  False)


        return {
            "responseCode": 200,
            "responseDescription": "Success",
            "responseMessage": multiple_user_schema.dump(page_object.items)
        }


