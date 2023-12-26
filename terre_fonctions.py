import os
import sys
import inspect

def create_alphabet():
    """
    Create a list with alphabet in lowercase.

    Returns:
        list: Alphabet in lowercase
    """
    alphabet = []

    for i in range(ord("a"), ord("z") + 1):
        alphabet.append(chr(i))
    
    return alphabet


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

def arguments_printer ():
    """
    Prints the given arguments line by line.
    
    Return:
        str : arguments
    """
    arguments = [i for i in sys.argv[1:]]

    for arg in arguments:
        print(arg)
    
def EH_argument_is_digit(arg):
    """
    Error Handling to verify the given argument is a digit, valid with +00 and -00. Meant to be used with a list.
    """
    if not (len(arg) == 1 and "".join(arg).lstrip("-+").isdigit()):
        print("erreur.")
        exit()

def even_odd(number):
    """
    Test an int, return even or odd.
    
    Return :
        str : even / odd
    """
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
