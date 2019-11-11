#!/usr/bin/python3

"""
Console Module to handle Objects
"""


from cmd import Cmd
from models import storage

class HBNBCommand(Cmd):
    """HBNBCommand Console class"""
    
    prompt = "(hbnb)"

    def do_quit(self, inp):
        """to quit from console"""
        return True

    def do_show(self, inp):
        """
        Prints the string representation of an 
        instance based on the class name and id
        """

        list_param = inp.split()

        if len(list_param) is 0:
            print('** class name missing **')
            return

        if list_param[0] != 'BaseModel':
            print('** class doesn\'t exist **')
            return

        if len(list_param) < 2:
            print('** instance id missing **')
            return

        obj_key = list_param[0] + "." + list_param[1]
        all_objs = storage.all()

        for key in all_objs.keys():
               
            if obj_key == key:
                print(all_abjs[obj_key])
                return

        print('** no instance found **')
        return

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
