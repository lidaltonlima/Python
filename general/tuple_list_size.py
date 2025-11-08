"""Compare sizes of tuples and lists"""
import sys

tuple_example = (1, 2, 3, 4, 5)
list_example = [1, 2, 3, 4, 5]
print(f'Tuple size: {sys.getsizeof(tuple_example)} bytes')
print(f'List size: {sys.getsizeof(list_example)} bytes')