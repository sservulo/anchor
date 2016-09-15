"""
System configuration constants
"""

RANGE_MIN = 1
RANGE_MAX = 100000

ENTRY_SIZE = 3
MAX_INPUT_SIZE = 99

ERROR_MSG_INVALID_FILE_EXTENSION = "The provided file has an invalid format. Only text (.txt) files are accepted."
ERROR_MSG_EXCEEDED_MAX_INPUT_SIZE = "Number of entries bigger than the allowed maximum (%d)." % MAX_INPUT_SIZE
ERROR_MSG_INPUT_SIZE_MISMATCH = "Mismatch between informed and actual number of entries."
ERROR_MSG_INVALID_ENTRY_SIZE = "Invalid entry size at line %d. Expected: %d per entry."
ERROR_MSG_INVALID_ENTRY_RANGE = "Invalid entry range at line %d."
ERROR_MSG_INVALID_ENTRY_TYPE = "Invalid input format at line %d. Only integers are accepted."
