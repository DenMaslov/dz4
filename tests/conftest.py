import pytest

from dz4.calculator.calculator import Calculator


@pytest.fixture()
def calculator() -> Calculator:
    return Calculator()



