#!/usr/bin/python3

"""
Console Module to handle Objects
"""


from cmd import Cmd

class HBNBCommand(Cmd):
    """HBNBCommand Console class"""
    
    prompt = "(hbnb)"



HBNBCommand().cmdloop()
