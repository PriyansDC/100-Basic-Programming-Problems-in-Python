# Write a program to replace all occurrences of a character with another character in a string.

w = input("Enter a word: ")

word = w.lower()
replace = "*"
new_word = ""

for i in word:
    if i in ('a', 'e', 'i', 'o', 'u'):
        new_word += replace
    else:
        new_word += i

print(new_word)