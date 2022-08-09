#!/usr/bin/python3
"""
file_storage:
Has a class FileStorage
"""


from genericpath import isfile
import json
""" from models.base_model import BaseModel """
import os.path


class FileStorage():
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        self.__objects["{}.{}".format(self.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        o_dict = {}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            for key, value in self.__objects.items():
                o_dict = {key: value.to_dict()}

            json.dump(o_dict, f)

    def reload(self):
        """"
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing. If the file doesnt exist,
        no exception should be raised
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path) as o_file:
                jso_line = o_file.read()
                obj_ct = self.__objects
                if jso_line:
                    diction = json.loads(jso_line)
                    for key, value in diction.items():
                        obj_ct[key] = eval(value[__name__])(**value)
