# Write a program to toggle the case of each character in a string.

word = input("Enter a word: ")

new_word = ""

for char in word:
    if 'a' <= char <= 'z':
        new_word += char.upper()

    elif 'A' <= char <= 'Z':
        new_word += char.lower()

    else:
        new_word += char

print(new_word)