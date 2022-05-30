import sqlalchemy
from .db_session import SqlAlchemyBase


class Category(SqlAlchemyBase):
    __tablename__ = 'category'
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False, primary_key=True)
    count = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)