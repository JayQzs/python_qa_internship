# Write a Python program calculate the product, multiplying all the numbers of a given tuple.
# Original Tuple:

nums = (4, 3, 2, 2, -1, 18)

import math
result = math.prod(nums)

#Product - multiplying all the numbers of the said tuple: -864
assert result == -864

# Write a Python program to convert a tuple of string values to a tuple of integer values.
# Original tuple values:
nums = (('333', '33'), ('1416', '55'))

def to_tuple_integer(input_tuple):
    return tuple(map(int, input_tuple))

def convert_tuple(input_tuple):
    return tuple(map(to_tuple_integer, input_tuple))

result = convert_tuple(nums)

assert result == ((333, 33), (1416, 55))

# Write a Python program to convert a given tuple of positive integers into an integer.
# Original tuple:
original = (1, 2, 3)

result = int("".join(map(str, original)))

assert result == 123

original = (10, 20, 40, 5, 70)

result = int("".join(map(str, original)))

assert result == 102040570