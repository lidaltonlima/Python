"""Docstring for the functions module"""
# from typing import Callable
from collections.abc import Callable


def with_callable(x: float, y: float, callback: Callable[[str], None]) -> None:
    """Function demonstrating callable type hinting"""
    result = x + y
    callback(str(result))

with_callable(10.5, 20.3, print) # outputs: 30.8


def with_args_kwargs(*args: int, **kwargs: str) -> None:
    """Function demonstrating *args and **kwargs type hinting"""
    print("Args:", args)
    print("Kwargs:", kwargs)

# outputs: Args: (1, 2, 3) Kwargs: {'name': 'Alice', 'city': 'Wonderland'}
with_args_kwargs(1, 2, 3, name="Alice", city="Wonderland")

def make_print(style: str) -> Callable[..., None]:
    """Function returning a callable with specific type hinting"""
    def printer(message: str) -> None:
        if style == "uppercase":
            print(message.upper())
        elif style == "lowercase":
            print(message.lower())
        else:
            print(message)
    return printer
