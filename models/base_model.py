#!/usr/bin/python3
"""BaseModel Module"""

import uuid
import datetime


class BaseModel:
    """
    BaseModel that defines all common
    attributes/methods for other classes:
    """

    id = None
    created_at = None
    updated_at = None

    def __init__(self, *args, **kwargs):
        """
        init method

        Args:
            Recieve keyworded and non keyworded args
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now().isoformat()

    def __str__(self):
        """
        str method

        Return: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[" + self.__class__.__name__ + \
            "] (" + self.id + ") " + str(self.__dict__)

    def save(self):
        """save method"""
        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        """
        to_dict method

        Return: dictionary containing all keys/values
        of __dict__ of an instance
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__

        return dictionary
