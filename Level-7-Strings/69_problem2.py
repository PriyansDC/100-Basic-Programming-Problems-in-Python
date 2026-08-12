# Write a program to count the number of vowels and consonants in a string.

n = input("Enter your favourite movie name: ")

vowel_count = 0
consonant_count = 0

vowel = ['a', 'e', 'i', 'o', 'u']

for i in n:
    if i in vowel:
        vowel_count += 1
    else:
        consonant_count += 1

print(f"Wow! {n} is mine favourite too.")
print(f"Vowel: {vowel_count} \nConsonant: {consonant_count}")