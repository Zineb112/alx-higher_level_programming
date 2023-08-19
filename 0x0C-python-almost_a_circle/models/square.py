#!/usr/bin/python3
""" Square module """

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method to update attributes based on arguments"""
        if args:
            arg_names = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(arg_names):
                    setattr(self, arg_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Override __str__ method to return a formatted string"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
