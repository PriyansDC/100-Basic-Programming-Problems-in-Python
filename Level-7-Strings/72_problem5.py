# Write a program to check whether a string is a palindrome.

word = input("Try to enter a palindrome word: ")

palindrome = ""

for i in range(len(word) - 1, -1, -1):
    palindrome += word[i]

print(f"Your given word is {word} and it's palindrome is {palindrome}")

if palindrome == word:
    print("Yes, it's a palindrome")
else:
    print("You can try once more!")