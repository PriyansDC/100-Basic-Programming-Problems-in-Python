# Write a program to find the sum of all odd numbers from 1 to n.

n = int(input("Enter a number: "))

result = 0

for i in range(1, n+1, 2):
    result += i

print(f"Sum of all odd numbers from 1 to {n}: {result}")