import pytest

from main import apply_discount, calculate_average, normalize_username


@pytest.mark.parametrize(
    ("price", "discount_percent", "expected"),
    [
        (100.0, 20.0, 80.0),
        (49.99, 10.0, 44.99),
        (80.0, 0.0, 80.0),
    ],
)
def test_apply_discount(price, discount_percent, expected):
    assert apply_discount(price, discount_percent) == expected


def test_calculate_average():
    assert calculate_average([10, 20, 30]) == 20.0


def test_calculate_average_with_one_value():
    assert calculate_average([8]) == 8.0


def test_calculate_average_empty_list():
    assert calculate_average([]) == 0.0


def test_normalize_username_trims_and_lowercases():
    assert normalize_username("  Ahmad  ") == "ahmad"


def test_normalize_username_without_outer_spaces():
    assert normalize_username("XAI") == "xai"
