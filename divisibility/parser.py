import os
from config import ERROR_MSG_INVALID_ENTRY_TYPE
from exception import InputError
import validator

"""
Parses a string into tokenized integers. Unformatted integer inputs raise ValueError during conversion.
Arguments:
    line - string (e.g. "7 2 4")
Returns:
    list of tokenized integers (e.g. [7,2,4])
"""
def parse_line(line):
    entry = [int(token) for token in line.split(' ')]
    return entry

"""
Parses a file into appropriate input format and validates it. Unformatted input raise InputError.
Arguments:
    file_f - file to be parsed
Returns:
    list of valid integers (e.g. [[7,2,4], [30,2,3]])
"""
def parse_file(file_f):
    #output
    parsed_data = []
    #line count for more explanatory raise exception
    line_count = 1
    input_size = None
    #parse each input line
    try:
        input_size = int(file_f.readline())
        for line in file_f:
            line_count += 1
            parsed_data.append(parse_line(line))
    except ValueError:
        raise InputError(ERROR_MSG_INVALID_ENTRY_TYPE % line_count)

    #validates data according to the according limits and argument sizes
    validator.validate(input_size, parsed_data)

    return parsed_data
