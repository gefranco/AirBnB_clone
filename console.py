#!/usr/bin/python3

"""
Console Module to handle Objects
"""


from cmd import Cmd

class HBNBCommand(Cmd):
    """HBNBCommand Console class"""
    
    prompt = "(hbnb)"

    def do_quit(self, inp):
        """to quit from console"""
        return True

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()