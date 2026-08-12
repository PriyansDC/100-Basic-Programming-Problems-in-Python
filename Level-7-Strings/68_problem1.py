# Write a program to find the length of a string without using an inbuilt function.

n = input("What's your name: ")

count = 0

for i in n:
    print(i)
    count += 1

print(f"The length of the given string {n}: {count}")