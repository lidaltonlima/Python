"""Checking types of variables."""
A = 'Hello, World!'
B = 42
C = 3.14

print(type(A), isinstance(A, str))  # Expected: <class 'str'>
print(type(B), isinstance(B, int))  # Expected: <class 'int'>
print(type(C), isinstance(C, int))  # Expected: <class 'float'>
