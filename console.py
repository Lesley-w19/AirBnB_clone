#!/usr/bin/python3
"""
    Console module
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Console
    """

    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, arg):
        raise SystemExit

    def do_EOF(self, arg):
        raise SystemExit

    def help_quit(self):
        print("Quit command to exit the program\n")

    def help_EOF(self):
        print("EOF(end of file) command to exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
