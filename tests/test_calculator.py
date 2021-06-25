""" Calculator module test cases """
import pytest
import math

from dz4.calculator.calculator import Calculator


valid_data = [
    (10, 5),
    (0, 3),
    (-1, -10),
]

invalid_data = [
    (1.3, 10),
    (5, 2.5),
    (11, "asd"),
]


@pytest.mark.parametrize('a, b', valid_data)
def test_add(calculator: Calculator, a: int, b: int):
    assert calculator.add(a, b) == a + b


@pytest.mark.parametrize('a, b', invalid_data)
def test_add_invalid(calculator: Calculator, a: int, b: int):
    with pytest.raises(TypeError):
        calculator.add(a, b)


@pytest.mark.parametrize('a, b', valid_data)
def test_subtract(calculator: Calculator, a: int, b: int):
    assert calculator.subtract(a, b) == a - b


@pytest.mark.parametrize('a, b', invalid_data)
def test_subtract_invalid(calculator: Calculator, a: int, b: int):
    with pytest.raises(TypeError):
        calculator.subtract(a, b)


@pytest.mark.parametrize('a, b', valid_data)
def test_divide(calculator: Calculator, a: int, b: int):
    assert calculator.divide(a, b) == a / b


@pytest.mark.parametrize('a, b', invalid_data)
def test_divide_invalid(calculator: Calculator, a: int, b: int):
    with pytest.raises(TypeError):
        calculator.divide(a, b)


def test_divide_by_zero(calculator: Calculator):
    with pytest.raises(ValueError):
        calculator.divide(10, 0)


@pytest.mark.parametrize('a, b', valid_data)
def test_multiply(calculator: Calculator, a: int, b: int):
    assert calculator.multiply(a, b) == a * b


@pytest.mark.parametrize('a, b', invalid_data)
def test_multiply_invalid(calculator: Calculator, a: int, b: int):
    with pytest.raises(TypeError):
        calculator.multiply(a, b)


@pytest.mark.parametrize('a, b', valid_data)
def test_mod(calculator: Calculator, a: int, b: int):
    assert calculator.mod(a, b) == a % b


@pytest.mark.parametrize('a, b', invalid_data)
def test_mod_invalid(calculator: Calculator, a: int, b: int):
    with pytest.raises(TypeError):
        calculator.mod(a, b)


def test_mod_zero(calculator: Calculator):
    with pytest.raises(ValueError):
        calculator.mod(100, 0)


@pytest.mark.parametrize('a, b', valid_data)
def test_power(calculator: Calculator, a: int, b: int):
    assert calculator.power(a, b) == a ** b


@pytest.mark.parametrize('a, b', invalid_data)
def test_power_invalid(calculator: Calculator, a: int, b: int):
    with pytest.raises(TypeError):
        calculator.power(a, b)

@pytest.mark.parametrize(
    'a',
    [10, 13, 100, 144, 9]
)
def test_root(calculator: Calculator, a: int):
    assert calculator.root(a) == math.sqrt(a)


@pytest.mark.parametrize(
    'a',
    [1.0, 1.3, "100", 1.44]
)
def test_root_invalid(calculator: Calculator, a: int):
    with pytest.raises(TypeError):
        calculator.root(a)


@pytest.mark.parametrize(
    'a',
    [-1.0, -3, -1.44]
)
def test_root_negative(calculator: Calculator, a: int):
    with pytest.raises(ValueError):
        calculator.root(a)
