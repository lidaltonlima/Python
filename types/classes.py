"""Docstring for the classes module"""
from abc import ABC, abstractmethod
from typing import Self, final, override
from dataclasses import dataclass, field


class BaseAddress(ABC):
    """Docstring for the BaseAddress class"""
    def __init__(self, street: str, number: int):
        """Docstring for __init__"""
        self.street = street
        self.number = number

    @abstractmethod
    def get_full_address(self) -> str:
        """Returns the full address as a string."""

class Address(BaseAddress):
    """Docstring for the Address class"""
    @override
    def get_full_address(self) -> str:
        return f'{self.street}, {self.number}'

@final
class CachedAddress(Address):
    """Docstring for the CachedAddress class"""
    def clone(self) -> Self: # Self type referencia à própria classe
        """Docstring for clone method"""
        return self


type Addresses = dict[int, Address]

@dataclass
class Person:
    """A class representing a person."""
    name: str
    age: int
    _addresses: Addresses = field(
        default_factory=dict[int, Address],
        init=False,
        repr=False
    )
    _new_address_index: int = 0

    def add_address(self, *addresses: Address) -> None:
        """Adds an address to the person's address book."""
        for address in addresses:
            self._addresses[self._new_address_index] = address
            self._new_address_index += 1


p1 = Address("Main St", 123)
