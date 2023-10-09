#!/usr/bin/python3
"""
Write a class MyInt that inherits from int:
"""


class MyInt(int):
    """
    MyInt is a rebel. MyInt has == and != operators inverted
    """

    def __eq__(self, other):
        """inverts equal method"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """inverts not equal method"""
        return not super().__ne__(other)
