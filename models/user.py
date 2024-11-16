#!/usr/bin/python3
"""Defines User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Inherits from BaseModel to define a user's details such as first_name,
    last_name, email and password

    Attributes:
        first_name (str): User's first name
        last_name (str): User's last name
        email (str): User's email address
        password (str): User's email password

    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """Instance init"""
        super().__init__(**kwargs)
