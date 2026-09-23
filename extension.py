import pytest


def double_integer(a: int) -> int:
    return a * 2


def add(a: float, b: float) -> float:
    return a + b


def calculate_discount(price: float, discount_percent: float) -> float:
    return price * (1 - discount_percent / 100)


def test_double_integer():
    assert double_integer(2) == 4
    assert double_integer(-5) == -10


def test_add():
    assert add(2, 3) == 5
    assert add(1.5, 2.5) == 4.0


def test_calculate_discount():
    assert calculate_discount(100, 20) == 80.0
    assert calculate_discount(50, 0) == 50.0