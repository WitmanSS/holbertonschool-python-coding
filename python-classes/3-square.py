#!/usr/bin/python3
"""Module that defines a Square class with size validation and area method."""


class Square:
    """Class that defines a square with controlled size attribute."""

    def __init__(self, size=0):
        """Initialize a square with a private size attribute.

        Args:
            size (int): Size of the square. Must be >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is < 0.
        """
        self.size = size  # Use setter for validation

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of th
