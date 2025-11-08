"""Example of regular expressions"""
import re

number = re.compile(r'(0)?(\+44)?\d{10}')  # Matches UK phone numbers with optional 0 or +44
num_1 = number.search('My number is +447999999999')
num_2 = number.search("My number is 07999999999")

print(num_1.group() if num_1 else "No match found for num_1")
print(num_2.group() if num_2 else "No match found for num_2")
