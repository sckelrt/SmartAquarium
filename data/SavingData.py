import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class SavingData(SqlAlchemyBase):
    __tablename__ = 'SavingData'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True)  # autoincrement=True)
    temp_air = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    humidity = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    temp_water = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    PH = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    volt = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    water = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    light = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    LIGH = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    Cooling = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    aquarium_id = sqlalchemy.Column(sqlalchemy.Integer)  # sqlalchemy.ForeignKey("Aquariums.id"))

    # Aquariums = orm.relation('Aquriums')
