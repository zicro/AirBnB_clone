#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

"""This Module is the BaseModel class defines all common
    attributes/methods for other classes
"""


class BaseModel:
    """Base Model class  defines all common attributes/methods
    for other classes used in AirBnB_clone
    """

    def __init__(self, *args, **kwargs):
        """initialization"""
        self.id = self._generate_id()
        self.created_at = self.updated_at = self._get_curr_time()

        if len(kwargs) != 0:
            self._assign_attributes(kwargs)
        else:
            from models import storage

            storage.new(self)

    def __str__(self):
        """prints the instance of the class in string type
        Returns:
            str: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """saves the instance atttributes of the class"""
        from models import storage

        self.updated_at = self._get_curr_time()
        storage.save()

    def to_dict(self):
        """creates a dictionary representation with
        “simple object type” of our BaseModel
        Returns:
            dict: A dictionary containing all keys and values of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

    @staticmethod
    def _generate_id():
        """Generate a unique identifier aka UUID"""
        return str(uuid4())

    @staticmethod
    def _get_curr_time():
        """Returns the current timestamp"""
        return datetime.today()

    def _assign_attributes(self, attrubutes):
        """Assigns the attrubutes from keyword arguments"""
        formatStr = "%Y-%m-%dT%H:%M:%S.%f"
        for key, value in attrubutes.items():
            if key == "created_at" or key == "updated_at":
                self.__dict__[key] = datetime.strptime(value, formatStr)
            else:
                self.__dict__[key] = value
