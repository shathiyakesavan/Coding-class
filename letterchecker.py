def is_alphabet(char):
 
    return 'a' <= char <= 'z' or 'A' <= char <= 'Z'


input_char = input("Enter a character: ")


if len(input_char) == 1:
    
    if is_alphabet(input_char):
        print(f"'{input_char}' is an alphabet.")
    else:
        print(f"'{input_char}' is not an alphabet.")
else:
    print("Please enter a single character.")