# Write a program to convert a string to uppercase and lowercase without inbuilt case functions.

sentence = input("Enter a string: ")

uppercase = ""
lowercase = ""

for char in sentence:

    ascii_value = ord(char)

    if 'a' <= char <= 'z':
        uppercase += chr(ascii_value - 32)
        lowercase += char

    elif 'A' <= char <= 'Z':
        uppercase += char
        lowercase += chr(ascii_value + 32)

    else:
        uppercase += char
        lowercase += char

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)