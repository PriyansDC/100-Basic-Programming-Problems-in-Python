# Write a program to read a character and check whether it is a vowel or a consonant.

char = "B"
vowel = ["a", "e", "i", "o", "u"]

if char.lower() in vowel:
    print("Vowel")
elif char not in vowel:
    print("Consonant")
else:
    print("Invalid")