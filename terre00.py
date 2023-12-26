#PRINT ALPHABET IN LOWERCASE


# Part 1 : Function 
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
    
# Part 2 : Display
print("".join(create_alphabet()))

print()