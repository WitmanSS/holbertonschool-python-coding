#!/usr/bin/python3
"""Module that defines a Square class with size validation and area method."""


class Square:
    """Class that defines a square with validated size."""

    def __init__(self, size=0):
        """Initialize a square with a private size attribute.

        Args:
            size (int): Size of the square. Must be >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is < 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size * self*
