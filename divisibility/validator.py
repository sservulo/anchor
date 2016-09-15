from config import *
from exception import InputError

"""
Helper function that verifies if a number num is within a range.
Arguments:
    minimum - int
    num - int
    maximum - int
Returns:
    boolean
"""
def valid_range(minimum, num, maximum):
    if(not(minimum < num and num < maximum)):
        return False
    return True

"""
Validates input data according to the according limits and argument sizes. Raises InputError otherwise.
Arguments:
    input_size - positive int
    input_data - list of lists (e.g. [[7,2,4],[30,2,3]])
Returns:
    None
"""
def validate(input_size, input_data):
    #verify if input is within max range
    if(input_size > MAX_INPUT_SIZE):
        raise InputError(ERROR_MSG_EXCEEDED_MAX_INPUT_SIZE)

    #verify if input_size corresponds to actual data size
    if(input_size != len(input_data)):
        raise InputError(ERROR_MSG_INPUT_SIZE_MISMATCH)

    #process each entry
    line_count = 1
    for entry in input_data:
        line_count += 1

        #verify if entry has appropriate size ENTRY_SIZE
        if(len(entry) != ENTRY_SIZE):
            raise InputError(ERROR_MSG_INVALID_ENTRY_SIZE % (line_count, ENTRY_SIZE))

        #verify if each entry number is within range
        n,x,y = entry
        if(not valid_range(RANGE_MIN, n, RANGE_MAX)
            or
            not valid_range(RANGE_MIN, x, n)
            or
            not valid_range(RANGE_MIN, y, n)):
            raise InputError(ERROR_MSG_INVALID_ENTRY_RANGE % line_count)
