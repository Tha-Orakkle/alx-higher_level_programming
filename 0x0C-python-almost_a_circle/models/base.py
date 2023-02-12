#!/usr/bin/python3
"""Defines a first class base"""
import json


class Base:
    """The Base model

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes a new Base

        Args:
            id (int): identity of the base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of a list of dicts

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """pass"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                dict_lists = [x.to_dictionary() for x in list_objs]
                jsonfile.write(Base.to_json_string(dict_lists))
