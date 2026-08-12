# Write a program to count the number of words in a sentence.

sentence = input("Tell me about your day in one sentence: ")

words = sentence.split()

word_count = 0

for i in words:
    word_count += 1

print(words)
print(f"Word count: {word_count}")
