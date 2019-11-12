#!/usr/bin/python3
"""BaseModel Module"""

from models.base_model import BaseModel

class State(BaseModel):
    """
    """
    name = ""

    def __init__(self, **kargs):
        """
        init method

        Args:
            Recieve keyworded and non keyworded args
        """

        super().__init__(**kargs)
            

    def to_dict(self):
        """
        to_dict method

        Return: dictionary containing all keys/values
        of __dict__ of an instance
        """
        dictionary = super().to_dict()

        dictionary["name"] = self.name
        return dictionary
