#!/usr/bin/Python3
from uuid import uuid4()
from datetime import datetime
"""BaseModel that defines all common attributes/methods for other classes:"""


class BaseModel:
    """Simple Base Model class"""
    def __init__(self, *args, **kwargs):
        """initialize imprtant instance attribute"""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        """dictionary representation of an instance (method to_dict())."""

        '''if len(kwargs) != 0:
            strft = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        self.__dict__[key] = datetime.strptime(value, strft)
                    else:
                        self.__dict__[key] = value
        else:
            models.storage.new(self) '''

    def save(self):
        """Update the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns the dict format of an object"""
        kvdict = self.__dict__.copy()
        # strtf = "%Y-%m-%dT%H:%M:%S.%f"
        kvdict["__class__"] = type(self).__name__
        kvdict["updated_at"] = self.updated_at.isoformat()
        kvdict["created_at"] = self.created_at.isoformat()
        return kvdict

    def __str__(self):
        """Returns information about the class in human readable format"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
