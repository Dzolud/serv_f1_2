import sqlalchemy
from .db_session import SqlAlchemyBase


class Form(SqlAlchemyBase):
    __tablename__ = 'forms'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    category_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    chat_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    category = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    photo = sqlalchemy.Column(sqlalchemy.JSON, nullable=False)
    video = sqlalchemy.Column(sqlalchemy.JSON, nullable=False)
