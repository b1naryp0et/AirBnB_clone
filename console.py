#!/usr/bin/python3
"""This is a class HBNBCommand"""
import cmd
import json
import shlex
from sys import argv
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""

    HBNBclasses = {"BaseModel": BaseModel, "User": User, "Place": Place,
                   "City": City, "State": State, "Amenity":
                   Amenity, "Review": Review}

    def do_create(self, arg):
        """create a new instance of BaseModel
        """
        if arg:
            if arg in HBNBCommand.HBNBclasses.keys():
                new = HBNBCommand.HBNBclasses[arg]()
                new.save()
                print(new.id)
        elif not arg:
            print("**class name missing **")
        else:
            print("** class doesn't exist **")
            
    def do_show(self, argv):
        """prints str rep of an instance based on class name & id
        """
        args = shlex.split(argv)

        if len(args) == 0:
            print("** class name missing **")
        elif len(args[0]) == "":
            print("** class name missing **")
        elif args[0] not in self.HBNBclasses:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args[1]) == "":
            print("** instance id missing **")
        else:
            a_dict = storage.all()
            key = args[0] + "." + args[1]
            if key in a_dict:
                print(a_dict[key])
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances based or not
        on the class name
        """
        nstance_list = []
        if line == "":
            for key, value in (storage.all()).items():
                print("key ->", key)
                print("value ->", value)
                nstance_list.append(value)
            print(nstance_list)
        elif line in self.HBNBclasses:
            for key, value in (storage.all()).items():
                if key == "{}.{}".format(line, value.id):
                    nstance_list.append(value)
            print(nstance_list)
        else:
            print("** class doesn't exist **")
    
    def do_count(self, line):
        """determine # of instances of specified class"""
        count_nstance = 0
        a_dict = storage.all()
        for key, value in a_dict.items():
            value = value.to_dict()
            if value['__class__'] == line:
                count_nstance += 1
        print(count_nstance)

    def do_destroy(self, argv):
        """delete instance based on the class name & id"""
        args = shlex.split(argv)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.HBNBclasses:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args[1]) == "":
            print("** instance id missing **")
        else:
            a_dict = storage.all()
            key = args[0] + "." + args[1]
            if key in a_dict:
                del a_dict[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_update(self, argv):
        """updates instance based on the class name and Id  
        """
        args = shlex.split(argv)

        if len(args) == 0:
            print("** class name missing **")
        if len(args[0]) == "":
            print("** class name missing **")
        elif args[0] not in self.HBNBclasses:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args[1]) == "":
            print("** instance id missing **")
        elif len(args) == 2:
            a_dict = storage.all()
            key = args[0] + "." + args[1]
            if key not in a_dict:
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            a_dict = storage.all()
            key = args[0] + "." + args[1]
            if key in a_dict:
                setattr(a_dict[key], args[2], args[3])
                storage.save()

    def emptyline(self):
        """Handle no input"""
        pass

    def do_quit(self, args):
        """Quit command to exit the program
        """
        raise SystemExit

    def do_EOF(self, line):
        """Exit"""
        print()
        return True

if __name__ == '__main__':
    display = HBNBCommand()
    display.prompt = "(hbnb) "
    display.cmdloop()
