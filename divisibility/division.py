from config import RANGE_MIN

"""
Verifies if a number is divisible by a divisor,
Arguments:
    num - int
    divisor - int
Returns:
    boolean
"""
def is_divisible(num, divisor):
    return num % divisor == 0

"""
Gets all numbers between RANGE_MIN and n that are divisible by x and not divisible by y.
Arguments:
    n - int
    x - int
    y - int
Returns:
    list of ints
"""
def get_divisible(n, x, y):
    numbers = []
    """
    This operation could be done in a more pythonic way with list comprehension, but to
    assure maintainability, this way seems more self explanatory.
    """
    for num in range(RANGE_MIN,n):
        if(is_divisible(num, x) and not is_divisible(num, y)):
            numbers.append(num)
    return numbers
