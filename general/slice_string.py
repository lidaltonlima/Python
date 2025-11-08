"""Test slice string"""
text = "Hello, World!"
print(text[7:12])  # Output: World
print(text[:5])    # Output: Hello
print(text[7:])    # Output: World!
print(text[-6:-1]) # Output: World
print(text[::2])   # Output: Hlo ol!
print(text[::-1])  # Output: !dlroW ,olleH
print(text[7:12:2]) # Output: Wrd
