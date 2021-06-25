""" Home task calculator module """
import math


class Calculator:
    """ Calculator implementation """
    def add(self, x: int, y: int) -> int:
        """ Add to attributes to each other """
        if self._are_args_int(x, y):
            return x + y
        self._rise_type_error()

    def subtract(self, x: int, y: int) -> int:
        """ Subtract one attribute from another """
        if self._are_args_int(x, y):
            return x - y
        self._rise_type_error()

    def divide(self, x: int, y: int) -> float:
        """ Divide x attribute on y """
        if y == 0:
            raise ValueError("Division by zero")
        if self._are_args_int(x, y):
            return x / y
        self._rise_type_error()

    def multiply(self, x: int, y: int) -> int:
        """ Multiply x attribute on y """
        if self._are_args_int(x, y):
            return x * y
        self._rise_type_error()

    def mod(self, x: int, y: int) -> int:
        """ Take mod of one attribute from another """
        if y == 0:
            raise ValueError("Division by zero")
        if self._are_args_int(x, y):
            return x % y
        self._rise_type_error()

    def power(self, x: int, y: int) -> int:
        """ Raise attributes x to a power y """
        if self._are_args_int(x, y):
            return x ** y
        self._rise_type_error()

    def root(self, x: int) -> float:
        """ Take a root from attributes """
        if x < 0:
            raise ValueError("Cannot compute root from negative")
        if isinstance(x, int):
            return math.sqrt(x)
        self._rise_type_error()

    def _are_args_int(self, x: any, y: any) -> bool:
        return isinstance(x, int) and isinstance(y, int)

    def _rise_type_error(self):
        raise TypeError("Arg must be an integer")


