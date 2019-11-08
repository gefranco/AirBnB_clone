#!/usr/bin/python3


import uuid
import datetime

class BaseModel:

    id = None
    created_at = None
    updated_at = None

    def __init__(self, *args, **kwargs):

            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now().isoformat()

    def __str__(self):
        return "[" + self.__class__.__name__ +"] ("+self.id + ") " + str(self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__

        return dictionary
