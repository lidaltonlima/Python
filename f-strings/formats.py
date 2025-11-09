"""Docstring for the formats module"""
TEXT = 'Hello, World!'
print(f'*{TEXT = !r}*') # Output: TEXT = 'Hello, World!'
print(f'*{TEXT:^20}*') # Output: TEXT =     Hello, World!
print(f'*{TEXT:>20}*') # Output: TEXT =     Hello, World!
print(f'*{TEXT:<20}*') # Output: TEXT =     Hello, World!
print(f'*{TEXT:=^20}*') # Output: TEXT =     Hello, World!
print(f'*{TEXT:.5}*')  # Output: *Hello*

NUMBER = 12345.6789
print(f'*{NUMBER:.2f}*')  # Output: *12345.68*
print(f'*{NUMBER:,.2f}*') # Output: *12,345.68*
print(f'*{NUMBER:_.2f}*') # Output: *12_345.68*
print(f'*{NUMBER:+.2f}*') # Output: *+12345.68*
print(f'*{NUMBER:-.2f}*') # Output: *12345.68*
print(f'*{NUMBER: .2f}*') # Output: * 12345.68*
print(f'*{NUMBER:0>10.2f}*') # Output: *0012345.68*
print(f'*{NUMBER:^15.2f}*') # Output: *   12345.68   *
print(f'*{NUMBER:e}*')  # Output: *1.234568e+04*
print(f'*{NUMBER:.3e}*')  # Output: *1.235e+04*
print(f'*{NUMBER:%}*')  # Output: *1234567.890000%*
print(f'*{NUMBER:.2%}*')  # Output: *1234567.89%*
print(f'*{NUMBER:.4g}*')  # Output: *1.2e+04*
print(f'*{NUMBER=}*')  # Output: *NUMBER=12345.6789*
