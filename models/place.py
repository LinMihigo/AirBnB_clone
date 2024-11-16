#!/usr/bin/python3
"""Defines the class - Place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Inherits from BaseModel to define a Place

    Attributes:
        city_id (str): City's id
        user_id (str): User's id
        name (str): State name
        description (str): Description of the place
        number_rooms (int): Place's number of rooms
        number_bathrooms (int): Place's number of bathrooms
        max_guest (int): Number of allowed guest
        price_by_night (int): Place price
        latitude (float): location latitude
        longitude (float): location longitude
        amenity_ids (list): string of Amenity ids

    """
    name = ''
    city_id = ''
    user_id = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Instance init"""
        super().__init__(**kwargs)
