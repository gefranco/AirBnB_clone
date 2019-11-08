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

                
        if kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key is not "__class__":
                    if key is "created_at" or key is "updated_at":
                        setattr(self, key, datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)


        elif args is not None and len(args) > 0:
            print("using args")

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            

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
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
