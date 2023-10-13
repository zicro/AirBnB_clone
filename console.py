#!/usr/bin/python3
""" This Module contains the entry point of the command interpreter """
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import re


class HBNBCommand(cmd.Cmd):
    """Cmd Interpreter
    Args:
        cmd (ob): object of the module cmd
    """

    prompt = "(hbnb) "
    __ALLOWED_CLASSES = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def arg_checker(self, args, id_needed=True):
        """Check the command line arguments"""
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif id_needed and len(args) == 1:
            print("** instance id missing **")
            return False
        elif args[0] not in HBNBCommand.__ALLOWED_CLASSES:
            print("** class doesn't exist **")
            return False
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel """
        args = shlex.split(arg)
        if not self.arg_checker(args, False):
            return
        new_instance = HBNBCommand.__ALLOWED_CLASSES[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        args = shlex.split(arg)
        if not self.arg_checker(args):
            return
        obj_dict = storage.all()
        key = args[0] + "." + args[1]
        self.print_instance(obj_dict, key)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = shlex.split(arg)
        if not self.arg_checker(args):
            return
        obj_dict = storage.all()
        key = args[0] + "." + args[1]
        self.del_instance(obj_dict, key)

    def do_all(self, arg):
        """Prints all string representation of all instances
        based on the class name"""
        args = shlex.split(arg)
        if len(args) == 0:
            self.print_all_instances(storage.all().values())
        elif not self.arg_checker(args, False):
            return
        else:
            self.print_all_instances_by_class(storage.all().values(), args[0])

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating an attribute """
        args = shlex.split(arg)
        if not self.arg_checker(args):
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        else:
            key = args[0] + "." + args[1]
            obj_dict = storage.all()
            self.update_instance_attr(obj_dict, key, args[2], args[3])

    def update_instance_attr(self, obj_dict, key, attr_name, attr_value):
        """Updates an attribute of an instance"""
        if key in obj_dict:
            if attr_name not in ["id", "created_at", "updated_at"]:
                if hasattr(obj_dict[key], attr_name):
                    attr_type = type(getattr(obj_dict[key], attr_name))
                    setattr(obj_dict[key], attr_name, attr_type(attr_value))
                else:
                    setattr(obj_dict[key], attr_name, attr_value)

                obj_dict[key].save()
            else:
                print("** attribute can't be updated **")
        else:
            print("** no instance found **")

    def del_instance(self, obj_dict, key):
        """ Deletes an instance from the object dictionary"""
        if key in obj_dict:
            del obj_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def print_all_instances(self, instances):
        """ Prints all the instances"""
        print([str(obj) for obj in instances])

    def print_all_instances_by_class(self, instances, class_name):
        """Prints the string representation of instances of
        a specific class"""
        print([str(obj)
               for obj in instances if obj.__class__.__name__ == class_name])

    def print_instance(self, obj_dict, key):
        """
        Prints the string of an instance
        """
        if key in obj_dict:
            print(obj_dict[key])
        else:
            print("** no instance found **")

    def do_quit(self, line):
        """Quit Command to exit the program"""
        return True

    def do_EOF(self, line):
        """Ctr-D exit the program"""
        print()
        return True

    def emptyline(self):
        """Ensures that empty line + ENTER doesn't execute anything"""
        pass

    def do_count(self, arg):
        """Counts the number of instances of a specific class"""
        count = 0
        for obj in storage.all().values():
            if arg == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, arg):
        command_map = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
        }
        match = re.search(r"\.(\w+)\((.*?)\)$", arg)
        if match is not None:
            class_name = arg[: match.start()]
            command = match.group(1)
            args = match.group(2).split(", ")
            if command in command_map.keys():
                if len(args) == 0:
                    full_command = "{} {}".format(command, class_name)
                elif len(args) == 1:
                    full_command = "{} {} {}".format(command,
                                                     class_name, args[0])
                elif len(args) == 3:
                    full_command = "{} {} {} {} {}".format(command,
                                                           class_name, args[0],
                                                           args[1], args[2])
                self.onecmd(full_command)
            else:
                print("{}: does not exit".format(arg))
        else:
            return cmd.Cmd.default(self, arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
