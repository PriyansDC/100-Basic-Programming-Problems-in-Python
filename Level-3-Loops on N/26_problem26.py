# Write a program to find the sum of all even numbers from 1 to n.

n = int(input("Enter a number: "))

result = 0

for i in range(0, n+1, 2):
    result += i

print("Sum of all even numbers from 1 to n: ", result)