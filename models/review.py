#!/usr/bin/python3
""" Review Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel

class Review(BaseModel, Base):
    __tablename__ = 'reviews'

    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    # Relationship to the User
    user = relationship("User", back_populates="reviews")

    # Relationship to the Place
    place = relationship("Place", back_populates="reviews")
