#!/usr/bin/python3
import models
import uuid
from datetime import datetime
""" a model that defines all common attributes/methods for other classes """


class BaseModel:
    """ simple class with name BaseModel for this project"""
    def __init__(self, *arg, **kwargs):
        """ Initialize instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        '''if len(kwargs) != 0:
            strtime = "%Y- %m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, strtime)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)'''

    def save(self):
        """ updates datetime of updated time to current time """
        self.updated_at = datetime.today()
        # models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values"""
        kdict = self.__dict__.copy()
        kdict["__class__"] = type(self).__name__
        kdict["created_at"] = self.created_at.isoformat()
        kdict["updated_at"] = self.updated_at.isoformat()
        return kdict

    def __str__(self):
        """ prints [<class name>] (<self.id>) <self.__dict__> """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
