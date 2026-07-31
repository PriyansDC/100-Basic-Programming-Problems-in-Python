# Write a program to display all prime numbers from 1 to n.

n = int(input("Enter a number: "))

for i in range(1, n):
    print("Outer:", i)

    for j in range(1, i):
        print("Inner:", j)