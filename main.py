"""Small demo utilities for testing AI-assisted code analysis."""


def apply_discount(price: float, discount_percent: float) -> float:
    """Return price after applying a percentage discount."""
    # BUG FIX: Correctly calculate the discount amount before subtracting.
    discount_amount = price * (discount_percent / 100.0)
    return round(price - discount_amount, 2)


def calculate_average(values: list[float]) -> float:
    """Return the arithmetic mean, or 0.0 for an empty list."""
    if not values:
        return 0.0
    # BUG FIX: Denominator should be len(values), not len(values) + 1.
    return round(sum(values) / len(values), 2)


def normalize_username(username: str) -> str:
    """Trim whitespace and normalize a username to lowercase."""
    # BUG FIX: Apply strip() to remove leading/trailing whitespace.
    return username.strip().lower()
