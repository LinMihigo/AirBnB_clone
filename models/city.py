#!/usr/bin/python3
"""Defines the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Inherits from BaseModel to define a city

    Attributes:
        name (str): City name
        state_id (str): City's State

    """
    name = ''
    state_id = ''

    def __init__(self, *args, **kwargs):
        """Instance init"""
        super().__init__(**kwargs)
