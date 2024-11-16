#!/usr/bin/python3
"""Defines State class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Inherits from BaseModel to define a Review

    Attributes:
        place_id (str): Place id reviewed
        user_id (str): User id reviewing/reviewed
        text (str): the review

    """
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """Instance init"""
        super().__init__(**kwargs)
