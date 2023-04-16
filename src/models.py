import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    firstname = Column(String, nullable=False)
    email = Column (String, nullable=False, unique=True)
    password = Column (String(10))    

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    element_id = Column (Integer, ForeignKey('elements.id'))

class Element (Base):
    __tablename__ = 'elements'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column (String)

class Planets(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    element_id = Column (Integer, ForeignKey('elements.id'))
    Terrain = Column(String)
    Climate = Column(String)
    Population = Column(Integer)
    Orbital_period = Column(Integer)
    Rotation_period = Column(Integer)
    Diameter = Column(Integer)

class Characters(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    element_id = Column (Integer, ForeignKey('elements.id'))
    Birth_Year = Column (Integer)
    Gender = Column (String)
    Height = Column (Integer)
    Hair_color = Column (String)
    Skin_color = Column (String)
    Eye_color = Column (String)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
