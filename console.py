#!/usr/bin/python3

"""
Console Module to handle Objects
"""


from cmd import Cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(Cmd):
    '''HBNBCommand Console class'''

    prompt = "(hbnb)"

    def do_quit(self, inp):
        '''Quit command to exit the program'''
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
                print(all_objs[obj_key])
                return

        print('** no instance found **')
        return

    do_EOF = do_quit

    def do_all(self, inp):
        '''Prints all string representation of all instances'''
        list_param = inp.split()

        if list_param[0] != 'BaseModel':
            print('** class doesn\'t exist **')
            return

        all_objs_list = []
        all_objs = storage.all()

        for key in all_objs.keys():

            all_objs_list.append(all_objs[key].__str__())

        print(all_objs_list)
        return

    def do_create(self, inp):
        '''Creates a new instance of BaseModel'''
        if inp == '':
            print('** class name missing **')
            return
        if inp != 'BaseModel':
            print("** class doesn't exist **")
            return
        base_model = BaseModel()
        base_model.save()
        print(base_model.id)

    def do_destroy(self, inp):
        '''Deletes an instance based on the class name and id'''
        if inp == '':
            print('** class name missing **')
            return
        list_param = inp.split()
        if list_param[0] != 'BaseModel':
            print("** class doesn't exist **")
            return
        if len(list_param) < 2:
            print("** instance id missing **")
            return

        key_object = list_param[0] + "." + list_param[1]
        all_objects = storage.all()
        if key_object not in all_objects:
            print("** no instance found **")
            return
        del all_objects[key_object]
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
