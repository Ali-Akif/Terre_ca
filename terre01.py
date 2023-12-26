# NAME OF THE FILE

import os
import sys


# Part 1 : Functions
def file_name_terminal():
    """
    Return the name of the current file, if executed other than by terminal 'python file_name.py', will print the file path. 
    
    Returns:
        str: File name
    """
    return sys.argv[0]

def file_name_cross_platform():
    """
    Return the name of the current file, ensuring cross-platform compatibility.
    
    Returns:
        str: File name.
    """
    return os.path.basename(__file__)


# Part 2 : Display
print(file_name_cross_platform())