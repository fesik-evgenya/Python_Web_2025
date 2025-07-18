import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class News(SqlAlchemyBase):
    __tablename__ = 'news'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True,
                           autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String,
                             nullable=True)
    content = sqlalchemy.Column(sqlalchemy.String,
                              nullable=True)
    create_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                    default=datetime.datetime.now())
    is_private = sqlalchemy.Column(sqlalchemy.Boolean,
                              default=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                        sqlalchemy.ForeignKey("users.id"))
    user = orm.relationship('User')

    def __repr__(self):
        return f'{self.id}: {self.title} = {self.content}>'
