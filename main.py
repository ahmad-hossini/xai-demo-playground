"""Small demo utilities for testing AI-assisted code analysis."""


def apply_discount(price: float, discount_percent: float) -> float:
    """Return price after applying a percentage discount."""
    # Fix: Calculate the discount amount as a percentage of the price.
    return round(price * (1 - discount_percent / 100), 2)


def calculate_average(values: list[float]) -> float:
    """Return the arithmetic mean, or 0.0 for an empty list."""
    if not values:
        return 0.0
    # Fix: Correct the denominator to be the actual number of values.
    return round(sum(values) / len(values), 2)


def normalize_username(username: str) -> str:
    """Trim whitespace and normalize a username to lowercase."""
    # Fix: Apply .strip() to remove leading/trailing whitespace.
    return username.strip().lower()
