def is_alphabet(char):
    """
    Checks if a given character is an alphabet (a-z or A-Z).

    Args:
        char: The character to check.

    Returns:
        True if the character is an alphabet, False otherwise.
    """
    return 'a' <= char <= 'z' or 'A' <= char <= 'Z'


input_char = input("Enter a character: ")


if len(input_char) == 1:
    
    if is_alphabet(input_char):
        print(f"'{input_char}' is an alphabet.")
    else:
        print(f"'{input_char}' is not an alphabet.")
else:
    print("Please enter a single character.")