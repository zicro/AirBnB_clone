#!/usr/bin/python3
"""Define the FileStorage class"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

CLASSES = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review,
}


class FileStorage:
    """serializes instances to a JSON file and deserializes
    JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dict __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = self._generate_key(obj)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        data_to_save = self._prepare_data_for_saving()
        self._write_to_file(data_to_save)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if not self.file_exists():
            return
        objs = self.load_from_file()
        self.create_objs(objs)

    @staticmethod
    def _generate_key(obj):
        """Generate key with format <obj class name>.id"""
        return obj.__class__.__name__ + "." + obj.id

    def _prepare_data_for_saving(self):
        """Prepare the data for saving by converting objects to dictionary"""
        return {k: v.to_dict() for k, v in FileStorage.__objects.items()}

    def _write_to_file(self, data):
        """Write the data to a JSON file"""
        with open(FileStorage.__file_path, "w") as f:
            json.dump(data, f)

    def file_exists(self):
        """check if the file exists"""
        return os.path.isfile(FileStorage.__file_path)

    def load_from_file(self):
        """Load data from file"""
        with open(FileStorage.__file_path, "r") as file_path:
            return json.load(file_path)

    def create_objs(self, objs):
        """Create objs from the loaded data"""
        FileStorage.__objects = {}
        for k in objs:
            name = k.split(".")[0]
            FileStorage.__objects[k] = CLASSES[name](**objs[k])
