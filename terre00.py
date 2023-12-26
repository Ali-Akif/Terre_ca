#PRINT ALPHABET IN LOWERCASE


# Part 1 : Function 
def alphabet_printer():
    """
    Print the alphabet in lowercase.
    
    Returns:
        str: alphabet
    """
    a = ord("a")
    z = ord("z")

    for i in range(a, z + 1):
        print(chr(i), end="")
    
# Part 2 : Display
alphabet_printer()