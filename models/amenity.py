#!/usr/bin/python3
"""Defines the class - Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Inherits from BaseModel to define Amenity class

    Attributes:
        name (str): Amenity name

    """
    name = ''

    def __init__(self, *args, **kwargs):
        """Instance init"""
        super().__init__(**kwargs)
