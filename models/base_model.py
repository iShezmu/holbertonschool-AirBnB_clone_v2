#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(Base):
    """A base class for all hbnb models"""

    __abstract__ = True

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            for key, value in kwargs.items():
                # Convert datetime fields from string to datetime object
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls_name = self.__class__.__name__
        return '[{}] ({}) {}'.format(cls_name, self.id, self.__dict__)

    def save(self):
        """Saves the object to the database"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.save()

    def delete(self):
        """Delete the object from the database"""
        from models import storage
        storage.delete(self)

    def to_dict(self):
        """Convert instance into dict format"""
        new_dict = {key: value for key,
                    value in self.__dict__.items()
                    if key != '_sa_instance_state'}
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
