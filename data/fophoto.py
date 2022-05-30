import sqlalchemy
from .db_session import SqlAlchemyBase


class Form_photo(SqlAlchemyBase):
    __tablename__ = 'photos'
    chat_id = sqlalchemy.Column(sqlalchemy.String, nullable=False, primary_key=True)
    count = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)