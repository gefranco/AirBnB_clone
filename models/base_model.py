#!/usr/bin/python3


import uuid
import datetime

class BaseModel:

    id = None
    created_at = None
    updated_at = None

    def __init__(self, *args, **kwargs):

                
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
        return "[" + self.__class__.__name__ +"] ("+self.id + ") " + str(self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
