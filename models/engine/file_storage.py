#!/usr/bin/python3
"""
file_storage:
Has a class FileStorage
"""

import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self, clas=None):
        """
        returns the dictionary __objects
        """
        if clas is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if clas == value.__class__ or clas == value.__class__.__name__ : new_dict[key] = value
                return new_dict
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """save the objects dictionary into file
        make serializable dict objects
        """
        with open(self.__file_path, "w") as f:
            json_object = {}
            json_object.update(self.__objects)
            for key, value in json_object.items():
                json_object[key] = value.to_dict()
            json.dump(json_object, f)

    def reload(self):
        """reload objects from file"""

        clses = {
            "BaseModel": BaseModel,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
            "User": User,
        }
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                o_dict = json.load(f)
                for ky, valu in o_dict.items():
                    self.new(clses[valu["__class__"]](**valu))
        except FileNotFoundError:
            return
