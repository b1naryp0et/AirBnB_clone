#!/usr/bin/python3

""" Base Model Module """

from datetime import datetime
import uuid
import models
import json

dtFrmt = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel:

    """ Airbnb base model class """

    def __init__(self, *args, **kwargs):
        """ Initiates BaseModel """

        if kwargs:
            self.id = kwargs["id"]
            self.created_at = datetime.strptime(kwargs.get("created_at"),
                                                dtFrmt)
            self.updated_at = datetime.strptime(kwargs.get("updated_at"),
                                                dtFrmt)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ The string representation of BaseModel """

        return "[{:s}] ({:s}) {}".format(type(self).__name__, self.id,
                                         self.__dict__)

    def __repr__(self):
        """ create and return formatted string """
        return self.__str__()

    def save(self):
        """ Date updater """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        ''' returns dictonary with all key values of instance '''
        a_dict = self.__dict__.copy()
        a_dict['__class__'] = self.__class__.__name__
        a_dict['created_at'] = self.created_at.isoformat()
        a_dict['updated_at'] = self.updated_at.isoformat()

        return a_dict
