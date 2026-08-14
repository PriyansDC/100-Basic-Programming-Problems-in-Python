# Write a program to count the frequency of each character in a string.

word = input("What's your favourite fast food: ")
n = word.lower()

word_checklist = []

for i in n:
    count = 0

    if i in word_checklist:
        continue

    word_checklist += i

    for j in n:

        if i == j:    
            if i == j:
                count += 1

    print(f"The frequency of letter {i} in {n}: {count}")
