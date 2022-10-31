#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    """
    instantiation of: id, created_at and update_at
    arguments: *args - pointer to list of commandline arguments
    **kwargs - list to key, value arguements.
    """

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        from models import storage

        if kwargs:
            for ky, valu in kwargs.items():
                if ky == "created_at" or ky == "updated_at":
                    self.__dict__[ky] = datetime.strptime(
                        valu, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[ky] = valu

        self.created_at = datetime.now()
        self.id = str(uuid.uuid4())
        self.updated_at = datetime.now()
        storage.new(self)

    def __str__(self):
        """
        Returns: string instance of BaseModel
        """
        return "[{:s}] ({:s}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        from models import storage

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of an instance.
        """

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
