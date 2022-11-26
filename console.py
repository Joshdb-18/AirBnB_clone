#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """Shouldn’t execute anything"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Should ecit the program"""
        print("")
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
