from data import db_session
from data.users import User
from flask import abort, jsonify
from flask_restful import reqparse, abort, Resource


parser = reqparse.RequestParser()
parser.add_argument('id', required=True, type=int)
parser.add_argument('name', required=True, type=str)
parser.add_argument('about', required=True, type=str)
parser.add_argument('email', required=True, type=str)
parser.add_argument('hashed_password', required=True, type=str)


def abort_if_news_not_found(users_id):
    db_session.global_init('db/blogs.db')
    session = db_session.create_session()
    users = session.query(User).get(users_id)
    if not users:
        abort(404, message=f"User {users_id} not found")


class UsersResource(Resource):
    db_session.global_init('db/blogs.db')

    def get(self, users_id):
        abort_if_news_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        session.close()
        return jsonify({'users': users.to_dict(
            only=('name', 'about', 'email', 'hashed_password', 'created_date'))})

    def delete(self, users_id):
        abort_if_news_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        session.delete(users)
        session.commit()
        session.close()
        return jsonify({'success': f'OK'})


class UsersListResource(Resource):
    db_session.global_init('db/blogs.db')

    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('id', 'name', 'about', 'email', 'hashed_password', 'created_date')) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        users = User()
        users.id = args['id']
        users.name = args['name']
        users.email = args['email']
        users.hashed_password = args['hashed_password']
        users.about = args['about']
        session.add(users)
        session.commit()
        return jsonify({'success': 'OK'})