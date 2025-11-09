"""Docstring for the performance module"""
# Basic string formatting comparison
import timeit


NAME = "Python"
VERSION = 3.9

# Using + operator (slowest for multiple items)
def concat_plus():
    """Doc"""
    return "Running " + NAME + " version " + str(VERSION)

# Using % formatting (old style)
def format_percent():
    """Doc"""
    return "Running %s version %s" % (NAME, VERSION) # pylint: disable=consider-using-f-string

# Using str.format()
def format_method():
    """Doc"""
    return "Running {} version {}".format(NAME, VERSION) # pylint: disable=consider-using-f-string

# Using f-string
def format_f_string():
    """Doc"""
    return f"Running {NAME} version {VERSION}"


# Let's time each method
print("Time taken (microseconds):")
print(f"+ operator: {timeit.timeit(concat_plus, number=10**6):.2f}")
print(f"% operator: {timeit.timeit(format_percent, number=10**6):.2f}")
print(f"str.format: {timeit.timeit(format_method, number=10**6):.2f}")
print(f"f-string:   {timeit.timeit(format_f_string, number=10**6):.2f}")
