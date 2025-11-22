#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Class that defines a square."""

    def __init__(self, size):
        """Initialize a square with a private size attribute.

        Args:
            size: The size of the square (no type/value validation).
        """
        self.__size = size

