from flask_restful import Resource

from api.users.UserSchema import UserSchema
from models.UserModel import UserModel

class UserController(Resource):
    
    def get(self):
        user_schema = UserSchema(many=True)
        result = user_schema.dump(list(UserModel.query.all()))

        return result.data, 200