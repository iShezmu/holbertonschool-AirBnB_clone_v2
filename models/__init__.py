#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

# Get the storage type from the enviroment variable
storage_type = os.getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    # If the environment variable is 'db', use DBStorage
    storage = DBStorage()
else:
    # Otherwise, default to FileStorage
    storage = FileStorage()

# Regardless of the storage type, call reload to load data
storage.reload()
