#!/usr/bin/python3
"""
State Module for HBNB project
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        @property
        def cities(self):
            """Return the list of City instances with state_id equal
            to the current State.id for FileStorage"""
            city_list = models.storage.all(City).values()
            return [city for city in city_list if city.state_id == self.id]
