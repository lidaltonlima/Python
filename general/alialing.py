"""Example of a aliasing in objects."""
a = [1, 2, 3]
b = a  # b is now an alias for a
b.append(4)
c = a.copy()  # c is a shallow copy of a
c.append(5)
print(a)  # Output: [1, 2, 3, 4]
print(b)  # Output: [1, 2, 3, 4]
print(c)  # Output: [1, 2, 3, 4, 5]