# Write a program to check whether two strings are anagrams of each other.

w1 = input("Enter a word of your choice: ")
w2 = input("Try to enter an anagram of it: ")

word1 = w1.lower()
word2 = w2.lower()

word_checklist_n = {}
word_checklist_ang = {}

for i in word1:
    count = 0

    if i in word_checklist_n:
        continue

    for j in word1:
        if i == j:
            count += 1

    word_checklist_n[i] = count

for i in word2:
    count = 0

    if i in word_checklist_ang:
        continue

    for j in word2:
        if i == j:
            count += 1

    word_checklist_ang[i] = count

if word_checklist_n == word_checklist_ang:
    print(f"{word1} and {word2} are anagrams of each other.")
else:
    print(f"{word1} and {word2} are not anagrams of each other.")