#!/usr/bin/python3
"""Defines the BaseModel class"""
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Public and private instance attributes init

        Args:
            ``*args`` (list): Variable length arg list (empty & unused)
            ``**kwargs`` (dict): Dictionary holding the instance attributes
            values
        """
        if kwargs:
            #: str: a unique id generated by the uuid module
            self.id = kwargs['id']
            #: str: Time of instance creation
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            #: str: Time instance is updated
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):  #: Returns a string representation of the Class Obj.
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):  #: Updates the public instance attr. updated_at
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
         Returns:
            dict: An obj containing all keys/values of obj(instance)'s
            writtable attributes.
        """
        self.__dict__['created_at'] = datetime.isoformat(self.__dict__['created_at'])
        self.__dict__['updated_at'] = datetime.isoformat(self.__dict__['updated_at'])
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__
