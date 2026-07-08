"""Utility functions for the Linkto backend."""

import secrets
import time

# Crockford's Base32 encoding (lowercase variant for username-friendliness)
CROCKFORD_BASE32 = "0123456789abcdefghjkmnpqrstvwxyz"


def generate_id(length: int = 8) -> str:
    """Generate a random ID using Crockford Base32.

    Default output is 8 characters.
    Example:
        7gk3m2qx
        b9z8f4hn
        1trw6kpd
    """
    return "".join(
        secrets.choice(CROCKFORD_BASE32)
        for _ in range(length)
    )