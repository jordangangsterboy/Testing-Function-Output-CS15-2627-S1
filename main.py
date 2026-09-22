import pytest


# --- 1. FUNCTIONS ---

def double_integer(a: int) -> int:
    """Double an integer."""
    return a * 2


def add(a: float, b: float) -> float:
    """Adds two numbers together."""
    return a + b


def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculates the final price after applying a percentage discount."""
    return price - (price * (discount_percent / 100))


# --- 2. TESTS ---

# Tests for double_integer (2 tests)
def test_double_integer_positive():
    assert double_integer(2) == 4

def test_double_integer_negative():
    assert double_integer(-5) == -10


# Tests for add (2 tests - including pytest.approx)
def test_add_integers():
    assert add(5, 10) == 15

def test_add_decimals():
    # Uses pytest.approx() to handle float precision issues
    assert add(0.1, 0.2) == pytest.approx(0.3)


# Tests for calculate_discount (2 tests)
def test_calculate_discount_standard():
    assert calculate_discount(100.0, 20.0) == 80.0

def test_calculate_discount_float():
    assert calculate_discount(49.99, 10.0) == pytest.approx(44.991)