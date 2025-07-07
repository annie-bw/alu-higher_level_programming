#!/usr/bin/python3
"""Defines a class Square with property getters and setters."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize the square with a size, using the setter for validation."""
        self.size = size  # Uses the setter method for validation

    @property
    def size(self):
        """Retrieve the current size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation.
        Args:
            value: The size to set.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2