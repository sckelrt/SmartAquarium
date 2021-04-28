import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class SavingData(SqlAlchemyBase):
    __tablename__ = 'Aquariums'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    login = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)