# Write a program to read a character and check whether it is an alphabet, digit or special symbol.

char = "4"

# Common special characters
special_characters = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*',
    '+', ',', '-', '.', '/', ':', ';', '<', '=', '>',
    '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|',
    '}', '~'
]

if char.isalpha():
    print("Alphabets")
elif char.isdigit():
    print("Digit")
elif char in special_characters:
    print("Special Character")
else:
    print("Invalid")