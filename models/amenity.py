#!/usr/bin/python3
""" Amenity Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    # The Many-To-Many relationship between places and amenities
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenities = relationship("Place",
                                       secondary=place_amenity,
                                       back_populates="amenities")
