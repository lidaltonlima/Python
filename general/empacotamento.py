"""Test unpacking"""
a, b, *c = [1, 2, 3, 4, 5]
print(f'a: {a}, b: {b}, c: {c}')  # Output: a: 1, b: 2, c: [3, 4, 5]
