# Write a program to count how many numbers from 1 to n are divisible by 3.

n = int(input("Enter a number: "))

count = 0

for i in range(1, n+1):
    if (i % 3 == 0):
        print(i, end=", ")
        count += 1
print(f"There are {count} numbers are divisible by 3 between 1 to {n}.")