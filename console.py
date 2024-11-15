#!/usr/bin/python3
"""Defines the HBNBCommand class"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage


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
        """Creates new class instance (BaseModel)"""
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

    def help_create(self):
        """Help docs - create"""
        print()
        print("*** Usage - create <ClassName>")
        text = """*** Creates instance of ClassName, saves it to file and
        prints its id"""
        print(text)
        print()

    def do_show(self, line):
        """
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

    def help_show(self):
        """Help docs - show"""
        print()
        print("*** Usage: show <ClassName> <instance id>")
        print("*** Prints a string repr. of an instance")
        print()

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
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

    def help_destroy(self):
        """Help docs - destroy"""
        print()
        print("*** Usage: destroy <ClassName> <instance id>")
        print("*** Deletes a ClassName instance with a specified instance id")
        print()

    def do_all(self, line):
        """
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

    def help_all(self):
        """Help docs - all"""
        print()
        print("*** Usage: all <ClassName>")
        text = """*** Prints str repr. of all instances. When ClassName is
        specified, instances printed are related to that class name"""
        print(text)
        print()

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute.

        Args:
            line (str): The command string
        """
        args = line.split()
        print()
        print(args)
        print()
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
                    print(f"Obj: {obj}")
                    print()
                    dict = obj.to_dict()
                    print(f"dict: {dict}")
                    print()
                    if args[2]:
                        if args[3]:
                            dict[args[2]] = args[3]
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                    print(f"Updated dict: {dict}")
                    print()
                    all_objs[key] = cls(**dict)
                    print(all_objs.get(key).to_dict())
                    print()
                    cls(**dict).save()
                else:
                    print("** no instance found **")

            else:
                print("** class doesn't exist **")

    def do_quit(self):
        """
        Exit the command interpreter

        Args:
            line (str): args passed to function
        """
        return True

    def help_quit(self):
        """Help docs - quit"""
        print("*** Usage: quit")
        print("*** Command to exit the command interpreter")

    def do_EOF(self, line):
        """
        Implements command exist upon reaching or calling EOF

        Args:
            line (str): args passed to function
        """
        print()
        return True

    def help_EOF(self):
        """Help docs - EOF"""
        print("*** Usage: Ctrl-D")
        print("*** Exit command interpreter")

    def emptyline(self):
        """Disables repetition of previous command on newline"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
