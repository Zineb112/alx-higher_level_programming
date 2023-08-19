#!/usr/bin/python3
""" Base module """

import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        filename = f"{class_name}.json"
        json_data = cls.to_json_string([obj.to_dictionary() for obj in list_objs])

        with open(filename, "w") as file:
            file.write(json_data)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
