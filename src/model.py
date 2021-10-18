from datetime import time
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float

Base = declarative_base()


class Sensor(Base):
    __tablename__ = "sensor"
    id = Column(Integer, primary_key=True)
    time = Column(DateTime())
    power = Column(Integer())
    temp = Column(Integer())
    humidity = Column(Integer())
    light = Column(Integer())
    CO2 = Column(Integer())
    dust = Column(Float())
