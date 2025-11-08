"""Typing examples."""
from dataclasses import dataclass
from typing import (Protocol, Callable, Any, Never, Literal, TypedDict, NotRequired, Required,
                    NamedTuple, Final, ClassVar, NoReturn, NewType)

# Type annotations in a dataclass /////////////////////////////////////////////////////////////////
@dataclass
class Person:
    """Type annotated dataclass example."""
    name: str
    age: int
    active: bool = False
    value_of_pi: ClassVar[float] = 3.14  # Class variable, not part of instance variables

people = Person('Doe', 30)
# people.value_of_pi = 3.14159 raise a type checker error
people.name = "Alice"
print(people.active)

# Protocol example //////////////////////////////////////////////////////////////////////////////
class Drawable(Protocol):
    """Verify if an object has a draw and delete method."""
    def draw(self) -> None:
        """Draw the object."""
    def delete(self) -> None:
        """Delete the object."""

class Circle:
    """Class implementing the Drawable protocol."""
    def draw(self) -> None:
        """Draw the circle."""
        print("Draw circle")

    def delete(self) -> None:
        """Delete the circle."""
        print("Delete circle")

class Square:
    """Class implementing the Drawable protocol."""
    def delete(self) -> None:
        """Delete the square."""
        print("Delete square")

def render(obj: Drawable) -> None:
    """Only accepts objects that implement the Drawable protocol."""
    obj.draw()

circle = Circle()
square = Square()
render(circle) # Only circle has draw and delete methods
# render(square) # This will raise a type checker error

# Basic type annotations //////////////////////////////////////////////////////////////////////////
a: int = 5
b: float = 3.2
c: str = "Hello"
h: bool = True
d: list[int] = [1, 2, 3]
e: dict[str, int] = {"one": 1, "two": 2, "three": 3}
f: tuple[int, str, float] = (1, "two", 3.0)
g: set[str] = {"apple", "banana", "cherry"}
m: Any = "Could be anything"

# Basic type annotations with typing library ******************************************************
l: Literal["apple", "banana", 5] = "banana"

# Union type annotation and type aliases **********************************************************
my_type = str | int | None
i: my_type = "Hello"
j: my_type = 5

# Function as type annotation /////////////////////////////////////////////////////////////////////
def apply_double(func: Callable[[int], int], value: int) -> int:
    """Apply a function to double the value."""
    return func(value)

def double(x: int) -> int:
    """Double the input value."""
    return x * 2

def multiply_three_numbers(x: int, y: int, z: int) -> int:
    """Multiply three numbers."""
    return x * y * z

print(apply_double(double, 5))  # Outputs: 10
# print(apply_double(multiply_three_numbers, 5)) # This will raise a type checker error

# Any and Never type annotations //////////////////////////////////////////////////////////////////
def process_data(data: Any) -> None:
    """Process data of any type."""
    print(f"Processing data: {data}")

def raise_error() -> Never:
    """Function that never returns."""
    raise ZeroDivisionError("This function always raises an error")

def no_return() -> NoReturn: # Do not use this. This as a last resort
    """Function that does not return."""
    raise RuntimeError("This function does not return anything")

# TypedDict example - Interface in JavaScript /////////////////////////////////////////////////////
class User(TypedDict): # class User(TypedDict, total=False): # all keys are optional
    """TypedDict example for user data."""
    name: str
    id: int
    is_active: bool
    email: NotRequired[str]  # Optional key

user1: User = {
    "name": "Alice",
    "id": 1,
    "is_active": True
}

class Config(TypedDict, total=False):
    """TypedDict example for configuration settings."""
    host: Required[str]
    port: int
    use_ssl: bool
    user: User # Nested TypedDict

config1: Config = {
    "host": "localhost",
    "port": 8080,
    "user": {
        "name": "Alice",
        "id": 1,
        "is_active": True
    }
}

# NamedTuple example //////////////////////////////////////////////////////////////////////////////
class Point(NamedTuple):
    """NamedTuple example for a point in 2D space."""
    name: str
    x: int
    y: int

point1 = Point("A", 10, 20)

PI: Final[float] = 3.14159  # Constant with type annotation
# PI = 3.14 # This will raise a type checker error

# NewType example /////////////////////////////////////////////////////////////////////////////////
UserId = NewType('UserId', int)
ProductId = NewType('ProductId', int)

def get_user_name(user_id: UserId) -> str:
    """Get user name by user ID."""
    return f"User{user_id}"
