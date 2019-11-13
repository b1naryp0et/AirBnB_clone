#!/usr/bin/python3
"""serializes instances to JSON file and deserializes JSON file to instances"""


import json

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

    def reload(self):
        """ Desirialization json """

        x = FileStorage.__file_path
        try:
            with open(x, "r", encoding="UTF-8") as f:
                y = json.load(f)
                for w, z in (y.items()):
                    z = eval(z["__class__"])(**z)
                    FileStorage.__objects[w] = z
        except FileNotFoundError:
            pass
