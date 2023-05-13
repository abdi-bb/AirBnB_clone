#!/usr/bin/python3
"""
A Console Module
"""


import cmd
import models
from models.base_model import BaseModel
import shlex
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """A Command Processor Class"""

    prompt = '(hbnb) '
    all_cls = [BaseModel, User, State, City, Amenity, Place, Review]

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

    def do_create(self, line):
        """Create an Object"""

        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in [c.__name__ for c in HBNBCommand.all_cls]:
                print("** class doesn't exist **")
                return
            else:
                obj = eval(class_name)()
                obj.save()
                print(obj.id)
        except Exception as e:
            print(e)

    def do_show(self, line):
        """Shows an Object"""

        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in [c.__name__ for c in HBNBCommand.all_cls]:
                print("** class doesn't exist **")
                return
            obj_id = args[1]
            if len(args) == 1:
                print("** instance id missing **")
            else:
                key = '{}.{}'.format(class_name, obj_id)
                objs = models.storage.all()
                if key in objs:
                    print(objs[key])
                else:
                    print("** no instance found **")
        except Exception as e:
            print(e)

    def do_destroy(self, line):
        """Destroy an Object"""

        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            if args[0] not in [c.__name__ for c in HBNBCommand.all_cls]:
                print("** class doesn't exist **")
                return
            else:
                objs = models.storage.all()
                for key, value in objs.items():
                    class_name = value.__class__.__name__
                    class_id = value.id
                    if class_name == args[0] and class_id == args[1]:
                        del value
                        del objs[key]
                        models.storage.save()
                        return
                print("** no instance found **")
        except Exception as e:
            print(e)

    def do_all(self, arg):
        """
        Prints all Objects
        """
        if not arg:
            objs = models.storage.all().values()
        else:
            try:
                cls = eval(arg)
                objs = [obj for obj in models.storage.all().values()
                        if type(obj) == cls]
            except NameError:
                print("** class doesn't exist **")
                return
        print([str(obj) for obj in objs])

    def do_update(self, line):
        """Update an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return
        args = shlex.split(line)
        if len(args) < 2:
            if len(args) == 1:
                print("** instance id missing **")
            else:
                print("** instance id missing **")
                print("** attribute name missing **")
            return
        class_name = args[0]
        id = args[1]
        models.storage.reload()
        objs = models.storage.all()
        key = "{}.{}".format(class_name, id)
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        value = args[3]
        try:
            value = eval(value)
        except Exception:
            pass
        if not isinstance(value, (str, int, float)):
            print("** only simple arguments can be updated **")
            return
        obj = objs[key]
        setattr(obj, attr_name, value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
