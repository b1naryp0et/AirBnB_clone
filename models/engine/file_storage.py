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

