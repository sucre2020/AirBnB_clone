#!/usr/bin/python3

"""this module is for the base class of the airbnb console project"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """class for the base model which other models will inherit from"""
    def __init__(self, *args, **kwargs):
        """ constructor for the class
            Args:
                id: (string) - assign with an uuid when an instance is created:
                created_at: (datetime) - assign with the current
                datetime when an instance is created
                updated_at: (datetime) - assign with the current
                datetime when an instance is created
                and it will be updated every time you change your object
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """string representation of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the public instance attribute updated_at
            with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
            of __dict__ of the instance"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
