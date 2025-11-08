"""Optimization."""
from time import time
from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    """Calculate Fibonacci numbers.

    Args:
        n (int): The position in the Fibonacci sequence.

    Returns:
        int: The Fibonacci number at position n.
    """
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


first = time()
# Without the decorator > 1.3 seconds
# With the decorator 0.00 seconds
a = fib(35)
last = time()
print(f"Fibonacci took {last - first:.2f} seconds and returned {a}")
