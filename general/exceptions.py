"""Exceptions examples."""
def get_ration(x: int, y: int) -> float:
    """Get the ratio of two numbers."""
    try:
        result = x / y
    except ZeroDivisionError:
        y = 1
        result = x / y
    return result

def divide_number(number_1: float, number_2: float) -> float | None:
    """Divide two numbers."""
    try:
        result = number_1 / number_2
        return result
    except ZeroDivisionError as error:
        print("You can't divide by zero")
        print(error)
        return None

print(get_ration(5, 0)) # 5.0
print(get_ration(5, 2)) # 2.5
divide_number(5, 0) # You can't divide by zero
