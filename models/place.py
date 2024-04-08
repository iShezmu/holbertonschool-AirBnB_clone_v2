#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
import models

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    # Relationship to the User
    user = relationship("User", back_populates="places")

    # For DBStorage: Relationship with Review
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", back_populates="place", cascade="all, delete, delete-orphan")
    else:
        # For FileStorage: Property to get reviews
        @property
        def reviews(self):
            """Get all reviews for this place when using FileStorage"""
            place_reviews = []
            all_reviews = models.storage.all(models.Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    place_reviews.append(review)
            return place_reviews
