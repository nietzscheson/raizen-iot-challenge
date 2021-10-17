import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Sensor(Base):
    __tablename__ = "sensor"
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
