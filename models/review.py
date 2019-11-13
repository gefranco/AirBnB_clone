#!/usr/bin/python3
"""review module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        init method

        Args:
            Recieve keyworded and non keyworded args
        """
        if kwargs is not None and len(kwargs) > 0:
            super.__init__(args, **kwargs)

        elif args is not None and len(args) > 0:
            print('im using args')

        else:
            super().__init__()

    def to_dict(self):
        """
        to_dict method

        Return: dictionary containing all keys/values
        of __dict__ of an instance
        """
        dictionary = super().to_dict()
        dictionary["place_id"] = self.place_id
        dictionary["user_id"] = self.user_id
        dictionary["text"] = self.text
        return dictionary
