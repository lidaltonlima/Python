"""Example of Lambda function handler."""
from typing import Callable

def sum_numbers(a: float, b: float) -> float:
    """Sum two numbers."""
    return a + b

sum_lambda: Callable[[float, float], float] = lambda a, b: a + b

print(f'Sum using function: {sum_numbers(3, 5)}')
print(f'Sum using lambda: {sum_lambda(3, 5)}')
