# Part 1 : Functions, Part 2 : Error Handling

import os
import sys
import inspect


# Part 1 : Functions

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


def hours12_to24(arg):
    arg = arg.zfill(7)


    if not( len(arg) == 7 and arg.replace(":", "").replace("PM", "").replace("AM","").isdigit() and arg.count(":") == 1 and arg.index(":") == 2 ):
        print("Merci de rentrer une heure en format : 12:30PM.")
        exit()
    elif not arg.index("M") == 6:
        print("Merci de de rentrer une heure au bon format, comme 12:30AM.")
        exit()

    liste = arg[:-2].split(":") + [arg[-2:]]

    hours, min, AM_PM = int(liste[0]), int(liste[1]), liste[2]

    if not ( 1<= hours <13 and min <60 ):
        print("C'est pas une heure ça frérot")
        exit()

    if AM_PM == "PM":
        if hours == 12:
            hours -=12
        else:
            hours += 12


    print(f"{'0' if hours < 10 else ''}{hours}:{min}")


def hours24_to_12(str):
    """
    Transform a string of 00:00 in 0:00AM or PM
    
    Returns:
        str : 0:00AM/PM
    """
    if not (len(str) == 5 and str.replace(":", "").isdigit() and str.count(":") == 1 and str.index(":") == 2):
        print("Merci de rentrer une heure au format HH:MM")
        exit()
    else:
        str = str.split(":")


    if int(str[0]) > 23:
        print("Merci de rentrer une heure valide.")
        exit()
    elif int(str[1]) > 59:
        print("Merci de rentrer une heure valide.")
        exit()
    else:
        hours = int(str[0])
        min = str[1]

    if hours > 12 or hours == 0:
        AM_PM = "PM"
    else:
        AM_PM = "AM"

    if AM_PM == "PM":
        if hours != 0:
            hours -= 12
    
    if hours == 0:
        hours += 12

    print(f"{hours}:{min}{AM_PM}")


# Part 2 : Error Handling Function
    
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