#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
import models

place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'),
           primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'),
           primary_key=True, nullable=False)
)


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

    user = relationship("User", back_populates="places")

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", back_populates="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 back_populates="place_amenities",
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """Get all reviews for this place when using FileStorage"""
            place_reviews = []
            all_reviews = models.storage.all(models.Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    place_reviews.append(review)
            return place_reviews

        @property
        def amenities(self):
            """Getter for amenities with FileStorage"""
            place_amenities = []
            all_amenities = models.storage.all(models.Amenity)
            for amenity in all_amenities.values():
                if amenity.id in self.amenity_ids:
                    place_amenities.append(amenity)
            return place_amenities

        @amenities.setter
        def amenities(self, obj):
            """
            Setter for amenities that adds an
            Amenity.id to the amenity_ids
            """
            if getenv('HBNB_TYPE_STORAGE') != 'db':
                if not isinstance(obj, models.Amenity):
                    return
                if not hasattr(self, 'amenity_ids'):
                    self.amenity_ids = []
                self.amenity_ids.append(obj.id)
