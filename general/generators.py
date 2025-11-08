"""Generators"""
import sys
from itertools import islice

a = [x * 2 for x in range(100)]
b = (x * 2 for x in range(100))

print(a)  # Output: [0, 2, 4, 6, 8, ..., 198]
print(b)  # Output: <generator object <genexpr> at ...>
print(f'List size: {sys.getsizeof(a)} bytes')  # Size of the list in bytes
print(f'Generator size: {sys.getsizeof(b)} bytes')  # Size of the generator in bytes

print(next(islice(b, 3, 4)))  # Output: 6
print(next(b))  # Output: 0
print(next(b))  # Output: 2
