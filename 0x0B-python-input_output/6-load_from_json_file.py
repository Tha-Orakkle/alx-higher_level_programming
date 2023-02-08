#!/usr/bin/python3
"""Defines a function that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """creates an object from a json file"""
    with open(filename) as f:
        json.load(f)
