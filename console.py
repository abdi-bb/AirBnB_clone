#!/usr/bin/python3
'''
Command Interpreter module
module: console
class: HBNBCommand
'''

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
    '''Command Interpreter class'''

    prompt = '(hbnb) '
    all_cls = [BaseModel, User, State, City, Amenity, Place, Review]

    def do_quit(self, line):
        '''Quit command to exit the program

        '''
        return True

    def do_EOF(self, line):
        '''EOF command to exit the program

        '''
        print()
        return True

    def emptyline(self):
        """Do nothing if line empty

        """
        pass

    def do_create(self, line):
        """Creates a new Object

        """

        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        try:
            class_name = args[0]
            if class_name not in [c.__name__ for c in HBNBCommand.all_cls]:
                print("** class doesn't exist **")
                return
            obj = eval(class_name)()
            obj.save()
            print(obj.id)
        except Exception as e:
            print(e)

    def do_show(self, line):
        """Show all Objects

        """

        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        try:
            class_name = args[0]
            if class_name not in [c.__name__ for c in HBNBCommand.all_cls]:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                obj_id = args[1]
                key = '{}.{}'.format(class_name, obj_id)
                objects = models.storage.all()
                if key in objects:
                    print(objects[key])
                else:
                    print('** no instance found **')
        except Exception as e:
            print(e)

    def do_destroy(self, line):
        """Destroy an Object

        """

        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return

        class_name = args[0]
        if class_name not in [c.__name__ for c in HBNBCommand.all_cls]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
            return

        objects = models.storage.all()
        try:
            obj_id = args[1]
            key = '{}.{}'.format(class_name, obj_id)
            obj = objects[key]
        except (KeyError, IndexError):
            print('** no instance found **')
            return

        del objects[key]
        models.storage.save()

    def do_all(self, line):
        """Prints all Objects.

        """

        if not line:
            objs = models.storage.all().values()
        else:
            try:
                cls = eval(line)
                objs = [obj for obj in models.storage.all().values()
                        if type(obj) == cls]
            except NameError:
                print("** class doesn't exist **")
                return
        print([str(obj) for obj in objs])

    def do_update(self, line):
        """Update an instance based on the class name and id

        """

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
