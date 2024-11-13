#!/usr/bin/python3
"""Defines the FileStorage class"""
import json
import os
from datetime import datetime


class FileStorage:
    """
    The FileStorage class serialises instances to JSON file and deserialises
    JSON file to instances.
    """
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """
        Instance methods init
        """
    def all(self):
        """
        Returns:
            dict: the __objects dict
        """
        return self.__objects
    
    def new(self, obj):
        """
        Appends obj to the __objects dict

        Args:
            obj (dict): Instance object (Contains writtable attributes of an
            instance) to append
        """
        print(obj.to_dict())
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()
    
    def save(self):
        """
        Serialises __objects to the json file
        """
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file)
    
    def reload(self):
        """
        Deserialises __file_path file to __objects
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
