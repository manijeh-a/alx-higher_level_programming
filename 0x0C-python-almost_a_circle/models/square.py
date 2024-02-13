#!/usr/bin/python3
"""identify a class Square"""


from inspect import classify_class_attrs
from models.rectangle import Rectangle


class Square(Rectangle):
    """example1: the Class that defines properties of Square.

     Attributes:
        width (int): the width of rectangle.
        height (int): the height of rectangle.
        x (int): x.
        y (int): y.
        id (int): it identity square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """example2: Creates new instances of Square

        Args:
            size (int): wthe idth and height of square.
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, optional): Identity number of square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """example3: Prints square"""
        return ("[Square] ({}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """example4: the Property retriever for size.

        Returns:
            int: the size of one side of square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """example5: the Property setter for width of square.
        Args:
            value (int): width of square.
        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """example6: it Assigns an argument to each attribute

        Args:
            *args (tuple): it arguments.
            **kwargs (dict): the double pointer to a dictionary.
        """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """example7: Returns dictionary representation of a Square.

        Returns:
            dict: the square.py.
        """
        dict1 = self.__dict__
        dict2 = {}
        dict2['id'] = dict1['id']
        dict2['size'] = dict1['_Rectangle__width']
        dict2['x'] = dict1['_Rectangle__x']
        dict2['y'] = dict1['_Rectangle__y']

        return dict2
