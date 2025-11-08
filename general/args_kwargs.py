"""Args and Keywords example."""
def some_function(*args: object, **kwargs: object) -> None:
    """Example function that takes any number of arguments and keyword arguments."""
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)

some_function(1, 2, 3, name="Alice", age=30)
