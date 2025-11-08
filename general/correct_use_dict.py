"""Get a value from a dictionary without a error."""
a = {'a': 1, 'b': 2}
print(a.get('a'))
print(a.get('c', 'this number does not exist'))
