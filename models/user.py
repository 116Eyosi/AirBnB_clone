#!/usr/bin/python3
"""
User class that is used for users
"""

import models


class User(models.BaseModel):
    """User class from base model
    Arttributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    Methods:
        __str__: prints the class name, id, and creates dictionary
        representations of the input values
        save(self): updates instance arttributes with current datetime
        to_dict(self): returns the dictionary values of the instance obj
    """

    def __str__(self):
        """
        Returns string representation of the class
        """

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
