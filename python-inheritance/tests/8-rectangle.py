#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        # Validate width and height using BaseGeometry's integer_validator
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Set private attributes
        self.__width = width
        self.__height = height
