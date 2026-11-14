"""Small demo utilities for testing AI-assisted code analysis."""


def apply_discount(price: float, discount_percent: float) -> float:
    """Return price after applying a percentage discount."""
    # Calculate the actual discount amount based on the percentage
    discount_amount = price * (discount_percent / 100.0)
    # Subtract the calculated discount from the original price
    return round(price - discount_amount, 2)


def calculate_average(values: list[float]) -> float:
    """Return the arithmetic mean, or 0.0 for an empty list."""
    if not values:
        return 0.0
    # INTENTIONAL DEMO BUG: denominator is one too large.
    return round(sum(values) / (len(values) + 1), 2)


def normalize_username(username: str) -> str:
    """Trim whitespace and normalize a username to lowercase."""
    # INTENTIONAL DEMO BUG: whitespace is not removed.
    return username.lower()
