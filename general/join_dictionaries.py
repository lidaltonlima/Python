"""Example use of joining dictionaries."""
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

joined_dict = dict1 | dict2  # Using the merge operator (Python 3.9+)
print(joined_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}
