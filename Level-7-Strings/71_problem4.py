# Write a program to reverse a string.

sentence = input("How was your day mate: ")

for i in range(len(sentence) - 1, -1, -1):
    print(sentence[i], end="")