from data import db_session
from data.works import Works
from flask import abort, jsonify
from flask_restful import reqparse, abort, Resource


parser = reqparse.RequestParser()
parser.add_argument('id', required=True, type=int)
parser.add_argument('title_of_activity', required=True, type=str)
parser.add_argument('team_leader', required=True, type=str)
parser.add_argument('work_size', required=True, type=int)
parser.add_argument('collaborators', required=True, type=str)
parser.add_argument('is_finished', required=True, type=bool)
parser.add_argument('user_id', required=True, type=int)


def abort_if_news_not_found(jobs_id):
    db_session.global_init('db/blogs.db')
    session = db_session.create_session()
    jobs = session.query(Works).get(jobs_id)
    if not jobs:
        abort(404, message=f"Job with id: {jobs_id} not found")


class JobsResource(Resource):
    db_session.global_init('db/blogs.db')

    def get(self, jobs_id):
        abort_if_news_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.query(Works).get(jobs_id)
        session.close()
        return jsonify({'jobs': jobs.to_dict(
            only=('id', 'title_of_activity',
                  'team_leader', 'work_size',
                  'collaborators', 'is_finished',
                  'user_id'))})

    def delete(self, jobs_id):
        abort_if_news_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.query(Works).get(jobs_id)
        session.delete(jobs)
        session.commit()
        session.close()
        return jsonify({'success': f'OK'})


class JobsListResource(Resource):
    db_session.global_init('db/blogs.db')

    def get(self):
        session = db_session.create_session()
        jobs = session.query(Works).all()
        return jsonify({'users': [item.to_dict(
            only=('id', 'title_of_activity',
                  'team_leader', 'work_size',
                  'collaborators', 'is_finished',
                  'user_id')) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        jobs = Works()
        jobs.id = args['id']
        jobs.title_of_activity = args['title_of_activity']
        jobs.team_leader = args['team_leader']
        jobs.work_size = args['work_size']
        jobs.collaborators = args['collaborators']
        jobs.is_finished = args['is_finished']
        jobs.user_id = args['user_id']
        session.add(jobs)
        session.commit()
        return jsonify({'success': 'OK'})