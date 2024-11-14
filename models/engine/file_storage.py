#!/usr/bin/python3
"""Defines the FileStorage class"""
import json
import os
import importlib


class FileStorage:
    """
    The FileStorage class serialises instances to JSON file and deserialises
    JSON file to instances.
    """
    __file_path = 'file.json'
    __objects = {}

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
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
    
    def save(self):
        """
        Serialises __objects to the json file
        """
        with open(self.__file_path, "w", encoding="utf-8") as file:
            d = {key: val.to_dict() for key, val in self.__objects.items()}
            json.dump(d, file)

    def reload(self):
        """
        Deserialises __file_path file to __objects
        """
        module_path = 'models.base_model'

        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                self.__objects.update(json.load(file))

        for key, value in self.__objects.items():
            class_name = value.pop('__class__')
            module = importlib.import_module(module_path)
            cls = getattr(module, class_name)
            self.__objects[key] = cls(**value)
