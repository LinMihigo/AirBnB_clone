#!/usr/bin/python3
"""Defines State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Inherits from BaseModel to define a State name

    Attributes:
        name (str): State name

    """
    name = ''

    def __init__(self, *args, **kwargs):
        """Instance init"""
        super().__init__(**kwargs)
