#!/usr/bin/python3
import json

"""
This is a module for to_json_string.
"""


def to_json_string(my_obj):
    """Return the JSON representation of an object (string)."""
    return(json.JSONEncoder().encode(my_obj))
