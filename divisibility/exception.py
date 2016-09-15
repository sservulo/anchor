"""
Base class for exceptions in this module.
This class was created for better extensibility should more features be added
and need treatment.
"""
class Error(Exception):
    pass

"""
Exception raised for errors in the input.

Attributes:
    msg  -- explanation of the error
"""
class InputError(Error):


    def __init__(self, msg):
        self.msg = msg
