"""Join lists into a dictionary."""
keys = ['name', 'age', 'city']
values: list[str | int] = ['Alice', 30, 'New York']
result = dict(zip(keys, values))
print("Joined dictionary:", result)
