#!/usr/bin/python3
"""
base_model:
defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """
    common attributes/methods
    """
    def __init__(self, *args, **kwargs):
        """
        instantiation of: id, created_at and update_at
        arguments: *args - pointer to list of commandline arguments
        **kwargs - list to key, value arguements.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs != None or  kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        models.storage.new(self)

    def __str__(self):
        """
        Returns: instance of BaseModel
        """
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        diction = self.__dict__.copy()
        diction['__class__'] = self.__class__.__name__
        diction['created_at'] = self.__dict__['created_at'].isoformat()
        diction['updated_at'] = self.__dict__['updated_at'].isoformat()

        return (diction)
