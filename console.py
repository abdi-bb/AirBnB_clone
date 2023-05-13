#!/usr/bin/python3
"""
A Console Module
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """A Command Processor Class"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""

        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""

        print()
        return True

    def emptyline(self):
        """Do nothing if empty line"""

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
