#!/usr/bin/python3
"""Defines the HBNBCommand class"""
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """
    Interpretes command strings into commands

    Attributes:
        prompt (str): custom prompt string that appears on each CLI line
    """
    prompt = '(hbnb) '

    def precmd(self, line):
        """Processes args passed at initialisation"""
        self._args = sys.argv[1:] if sys.argv[1:] else line.strip().split()
        return " ".join([arg.strip('" ') for arg in self._args])

    def do_create(self, line):
        """
        *** Usage - create <ClassName>
        Creates new class instance based on ClassName

        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            if args[0] in globals() and isinstance(globals()[args[0]], type):
                cls = globals()[args[0]]()
                cls.save()
                print(cls.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """
        ***Usage: show <ClassName> <instance id>
        Prints a string repr. of an instance based on the class name and id

        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            if args[0] in globals() and isinstance(globals()[args[0]], type):
                all_objs = storage.all()
                key = f"{args[0]}.{args[1]}"
                if key in all_objs:
                    print(all_objs[key])
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """
        *** Usage: destroy <ClassName> <instance id>
        Deletes an instance based on the class name and id

        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            if args[0] in globals() and isinstance(globals()[args[0]], type):
                all_objs = storage.all()

                key = f"{args[0]}.{args[1]}"
                if key in all_objs:
                    all_objs = {k: v for k, v in all_objs.items() if k != key}
                else:
                    print("** no instance found **")

                storage.update_objects(all_objs)
                storage.save()
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """
        *** Usage: all <ClassName>
            or: <ClassName>.all()
        Prints all string repr. of all instances based on or not on the class
        name

        Args:
            line (str): command string
        """
        args = line.split()
        all_objs = storage.all()
        values = list(all_objs.values())

        if len(args) == 0:
            print([str(val) for val in values])
        else:
            if args[0] in globals() and isinstance(globals()[args[0]], type):
                print([str(val)
                       for val in values if val.__class__.__name__ == args[0]])
            else:
                print("** class doesn't exit **")

    def do_count(self, line):
        """
        *** Usage: count <ClassName>
            or: <ClassName>.count() (Preferred)
        Counts number of instances of a class

        Args:
            line (str): string containing name of class
        """
        args = line.split()
        all_objs = storage.all()
        val = list(all_objs.values())

        if len(args) == 0:
            print(f"{len(val)}")
        else:
            if args[0] in globals() and isinstance(globals()[args[0]], type):
                length = len([v
                              for v in val if v.__class__.__name__ == args[0]
                              ])
                print(f"{length}")
            else:
                print("** class doesn't exit **")

    def do_update(self, line):
        """
        *** Usage: update <ClassName> <instance id> <attr> <value>
        Creates and updates an instance based on the class name and id by
        adding or updating attribute.

        Args:
            line (str): The command string
        """
        args = line.split()
        print(args)
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            if args[0] in globals() and isinstance(globals()[args[0]], type):
                all_objs = storage.all()

                key = f"{args[0]}.{args[1]}"
                if key in all_objs:
                    cls = globals()[args[0]]
                    obj = all_objs[key]

                    dict = obj.to_dict()
                    if args[2]:
                        if args[3]:
                            dict[args[2]] = args[3]
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")

                    all_objs[key] = cls(**dict)

                    cls(**dict).save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_quit(self, line):
        """
        *** Usage: quit
        Exit the command interpreter

        Args:
            line (str): args passed to function
        """
        return True

    def do_EOF(self, line):
        """
        *** Usage: Ctrl-D
        Implements command exist upon reaching or calling EOF

        Args:
            line (str): args passed to function
        """
        print()
        return True

    def emptyline(self):
        """Disables repetition of previous command on newline"""
        pass

    def default(self, line):
        """Handles unconventional command formats"""
        if "." in line:
            str = re.match(r"(\w+)\.(.+)", line)
            class_name, command = str.group(1), str.group(2).strip()

            if command == "all()":
                self.do_all(class_name)
            elif command == "count()":
                self.do_count(class_name)
            elif command[:5] == "show(":
                match = re.match(r"show\(\"(.*?)\"\)", command)
                args = list(match.groups()) if match else None
                if args:
                    line = " ".join([class_name, args[0]])
                else:
                    line = class_name
                self.do_show(line)
            elif command[:8] == "destroy(":
                match = re.match(r"destroy\(\"(.*?)\"\)", command)
                if match:
                    args = list(match.groups())
                if args:
                    line = " ".join([class_name, args[0]])
                else:
                    line = class_name
                self.do_destroy(line)
            else:
                print(f"Unknown syntax: {line}")
        else:
            print(f"Unknown syntax: {line}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
