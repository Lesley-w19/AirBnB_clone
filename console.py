#!/usr/bin/python3
"""
    Console module
"""

import cmd
from models.base_model import BaseModel
import json

class HBNBCommand(cmd.Cmd):
    """ Console prompt  """
    prompt = "(hbnb) "

    """ --Classes """
    __classes = ['BaseModel']


    """ --Commands """
    __commands = ['create', 'show', 'destroy', 'all', 'update']


    def emptyline(self):
        """do nothing when empty"""
        pass

    def do_quit(self, arg):
        """exit program when arg is quit"""
        raise SystemExit

    def do_EOF(self, arg):
        """exits program when arg is EOF"""
        raise SystemExit
    
    def do_create(self, prmArg):
        """
        creates a new instance of BaseModel, 
        saves it to the JSON file and prints the id.
        """
        if not prmArg:
            raise ValueError("** class name missing **")
        elif prmArg not in self.__classes:
            raise ValueError("** class doesn't exist **")
        else:
            model_classes = {'BaseModel': BaseModel}
            my_model = model_classes[prmArg]()
            print(my_model.id)
            storage.save()    

    def help_quit(self):
        print("Quit command to exit the program\n")

    def help_EOF(self):
        print("EOF(end of file) command to exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
