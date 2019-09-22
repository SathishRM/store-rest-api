from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='Mandatory Field')
    parser.add_argument('password', type=str, required=True, help='Mandatory Field')

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {'message': 'User-{} is already exists in the system'.format(data['username'])}, 400
        user = UserModel(**data)  # *data=data['username'],data['password']
        print(user.username, user.password)
        user.save_to_db()
        return {'message': 'User-{} has created successfully'.format(data['username'])}, 201
