from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class Energy(Base):
    __tablename__ = 'energy'
    id = Column(Integer, primary_key=True)
    country = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    consumption = Column(Float, nullable=False)

class Transport(Base):
    __tablename__ = 'transport'
    id = Column(Integer, primary_key=True)
    country = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    vehicles = Column(Integer, nullable=False)

class Water(Base):
    __tablename__ = 'water'
    id = Column(Integer, primary_key=True)
    country = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    usage = Column(Float, nullable=False)
