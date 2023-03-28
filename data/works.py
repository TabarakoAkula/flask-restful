import datetime
import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Works(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'works'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title_of_activity = sqlalchemy.Column(sqlalchemy.String, default=None)
    team_leader = sqlalchemy.Column(sqlalchemy.String, default=None)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, default=None)
    collaborators = sqlalchemy.Column(sqlalchemy.String, default=None)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=None)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"), default=None)
    user = orm.relationship('User')
    categories = orm.relationship("Category",
                                  secondary="association",
                                  backref="works")