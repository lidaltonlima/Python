"""Docstring for the basic_types module"""
from typing import Final


# One value
name: str = "Type Hints Example"
age: int = 30
number: float = 99.99
is_active: bool = True
data: bytes = b"example"

# Multiple values
names: list[str] = ["Alice", "Bob", "Charlie"]
ages: tuple[int, int, int, str] = (25, 30, 35, '40')
ages2: tuple[int, ...] = (25, 30, 35, 40, 45)
weights: set[float] = {55.5, 65.0, 75.2}
weights_immutable: frozenset[float] = frozenset({55.5, 65.0, 75.2})
scores: dict[str, int] = {"Alice": 90, "Bob": 85, "Charlie": 95}
numbers: range = range(1, 10)
not_value: None = None
all_values: object = "Can be any type"
type_example: type[int] = int
type_any: type = str
CONSTANT = 3.14 # Don't use Final here, just a convention
CONSTANT_LIST: Final[list[int]] = [1, 2, 3, 4, 5]
constant: Final[int] = 100  # pylint: disable=invalid-name
