import os
import sys
import inspect


# FUNCTIONS

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

def result_remain(a, b):
    """
    Print the result of a // division and the remain with % 
    
    Returns: 
        str : Result: a // b \n Remain : a % b
    """
    if b > a:
        print("error.")
    elif b == 0:
        print("error")
    else:
        print(f"""Result : {a // b}
Remain : {a % b}""") 

def reverse_string(string):
    """
    Reverse a string
    
    Returns:
        print reverse string
    """
    reverse_string = ""
    for i in string:
        reverse_string = i + reverse_string
    print(reverse_string)

def power(base, exponent):
    """
    Multiply a base to the power of the exponent without using **
    
    returns : 
        int : results
    """
    if exponent < 1:
        print("error.")
        exit()

    results = base

    for i in range(exponent -1): # -1 because if we do a power of 3rd, we only multiply the number by itself 2 times
        results *= base
    
    print(results)

def sqrt_positive_int(radicant):
    """
    Print the square root of a positive integer.
    
    Returns:
        str : square root
    """
    if radicant > 1:
        print(radicant ** 0.5)
    else:
        print("error.")
        exit()

def prime_number(number):
    """
    Print if a number is prime or not, function with an int

    Returns:
        str : {number} is / is not / a prime number.
    """
    common_factor = 0
    for i in range(1, number + 1):
        if number % i == 0:
            common_factor += 1
    
    if common_factor ==  2 and number != 1:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
        
# Error Handling Function
    
def EH_argument_lenght(arg, a):
    """
    Verify the lenght of a list
    """
    if not len(arg) == a:
        print("error.")
        exit()

def EH_argument_lenght_and_is_digit(arg, a):
    """
    Error Handling to verify the given argument is a digit, valid with +00 and -00. Meant to be used with a list. a is for the number of arguments desired
    """
    if not (len(arg) == a and "".join(arg).lstrip("-+").isdigit()):
        print("error.")
        exit()

def EH_string_not_only_digit(string):
    if string.isdigit():
        print("error.")
        exit()