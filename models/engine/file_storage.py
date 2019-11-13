#!/usr/bin/python3
"""serializes instances to JSON file and deserializes JSON file to instances"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ Class for FileStorage """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns the objects dictionary """

        return FileStorage.__objects

    def new(self, obj):
        """ Returns class name and instance """

        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ serializes __objects to Json file """
        a_dict = {}
        for key in FileStorage.__objects:
            a_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, mode="w",
                encoding="utf-8") as a_file:
            json.dump(a_dict, a_file)

    def reload(self):
        """ Desirialization json """
        try:
            with open(FileStorage.__file_path, mode="r",
                    encoding="utf-8") as a_file:
                a_dict = json.load(a_file)
            for key, value in a_dict.items():
                FileStorage.__objects[key] = eval(value['__class__'])(**value)
        except FileNotFoundError: pass
