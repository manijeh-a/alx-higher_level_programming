#!/usr/bin/python3
"""Function add_attribute"""


def add_attribute(obj, attr_name, value):
    """Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to which the attribute will be added.
        attr_name: The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object can't have a new attribute.
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attr_name, value)
