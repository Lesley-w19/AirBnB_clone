#!/usr/bin/python3
"""
base_model:
defines all common attributes/methods for other classes
"""

import uuid
from datetime import datetime

# from models import storage


class BaseModel:
    """
    common attributes/methods
    """

    def __init__(self, *args, **kwargs):
        """
        instantiation of: id, created_at and update_at
        arguments: *args - pointer to list of commandline arguments
        **kwargs - list to key, value arguements.
        """

        if kwargs is not None and kwargs != {}:
            time_frmt = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        value, time_frmt)
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        value, time_frmt)
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    #            storage.new(self)

    def __str__(self):
        """
        Returns: instance of BaseModel
        """

        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """

        self.updated_at = datetime.now()

    #        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of an instance."""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
