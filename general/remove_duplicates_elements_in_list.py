"""Example of removing duplicate elements from a list"""
a = [1, 1, 2, 3, 1, 2, 4, 5, 5, 5, 6]
print(list(set(a)))  # Output: [1, 2, 3, 4, 5] (order may vary)
