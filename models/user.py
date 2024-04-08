#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel

class User(BaseModel, Base):
    """Representation of a user"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    # Relationship between User and Place
    places = relationship("Place", back_populates="user", cascade="all, delete, delete-orphan")

    # Relationship between User and Review
    reviews = relationship("Review", back_populates="user", cascade="all, delete, delete-orphan")
