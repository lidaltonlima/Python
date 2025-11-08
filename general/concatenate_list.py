"""Concatenate list example."""
A: list[str] = ['One', 'two', 'three']
B: list[str] = ['One', 'two', 'three']
C: list[str] = A + ['four'] + A
print(A)
print(B)
print(C)
