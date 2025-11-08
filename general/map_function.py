"""Map function examples."""
def is_value_string(value: object) -> bool:
    """Check if a value is a string."""
    return isinstance(value, str)

list_: list[float | str] = [1, '2', 3, '4', 5]
print(list(map(is_value_string, list_)))
