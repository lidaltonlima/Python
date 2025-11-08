"""Example for math operations module."""
import math

# Basic Math Operations ///////////////////////////////////////////////////////////////////////////
print(f'Sum: 5 + 10 = {5 + 10}')  # Outputs: 15
print(f'Difference: 10 - 5 = {10 - 5}')  # Outputs: 5
print(f'Product: 5 * 10 = {5 * 10}')  # Outputs: 50
print(f'Quotient: 10 / 5 = {10 / 5}')  # Outputs: 2.0
print(f'Floor Division: 10 // 3 = {10 // 3}')  # Outputs: 3
print(f'Modulus: 10 % 3 = {10 % 3}')  # Outputs: 1
print(f'Exponentiation: 2 ** 3 = {2 ** 3}')  # Outputs: 8

# Using math module ///////////////////////////////////////////////////////////////////////////////
# Number-theoretic functions
print(f'Combination: C(5, 3) = {math.comb(5, 3)}')  # Outputs: 10
print(f'Permutation: P(5, 3) = {math.perm(5, 3)}')  # Outputs: 60
print(f'Factorial: 5! = {math.factorial(5)}')  # Outputs: 120
print(f'GCD of 48 and 18 = {math.gcd(48, 18)}')  # Outputs: 6
print(f'LCM of 4 and 5 = {math.lcm(4, 5)}')  # Outputs: 20
print(f'Isqrt of 16 = {math.isqrt(16)}')  # Outputs: 4
