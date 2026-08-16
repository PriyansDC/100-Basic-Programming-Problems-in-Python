# Write a program to find the first non-repeating character in a string.

word = input("Enter a word: ")

word_checklist = {}
print(type(word_checklist))

for i in word:
    count = 0

    if i in word_checklist:
        continue

    for j in word:
        if i == j:
            count += 1

    word_checklist[i] = count

for i in word_checklist:
    if word_checklist[i] == 1:
        print(f"The first non-repeating character in {word} is {i}")

        break