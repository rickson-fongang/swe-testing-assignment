import pytest
from quick_calc.calculator import Calculator

calc = Calculator()

def test_addition():
    assert calc.add(5, 3) == 8

def test_subtraction():
    assert calc.subtract(10, 4) == 6

def test_multiplication():
    assert calc.multiply(6, 7) == 42

def test_division():
    assert calc.divide(8, 2) == 4

def test_division_by_zero():
    with pytest.raises(ValueError):
        calc.divide(5, 0)

def test_negative_numbers():
    assert calc.add(-5, -3) == -8

def test_decimal_numbers():
    assert calc.multiply(2.5, 2) == 5.0

def test_large_numbers():
    assert calc.multiply(1_000_000, 2) == 2_000_000