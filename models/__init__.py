#!/usr/bin/python3
"""
This module handles imports

A variable to store the instance of FileStorage is created.
The reload method is then called on the instance variable.

Attributes:
    storage (dict): An instance of FileStorage
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
