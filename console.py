#!/usr/bin/python3

"""
Console Module to handle Objects
"""


from cmd import Cmd
from models.base_model import BaseModel
class HBNBCommand(Cmd):
    '''HBNBCommand Console class'''
    
    prompt = "(hbnb)"

    def do_quit(self, inp):
        '''Quit command to exit the program'''
        return True

    do_EOF = do_quit

    def do_create(self, inp):
        '''Creates a new instance of BaseModel'''
        if inp == '':
            print('** class name missing **')
            return
        if inp != 'BaseModel':
            print("** class doesn't exist **")
            return
        base_model = BaseModel()
        print(base_model.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
