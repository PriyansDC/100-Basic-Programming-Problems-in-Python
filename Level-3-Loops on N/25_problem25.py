# Write a program to find the sum of all natural numbers from 1 to n.

n = int(input("Enter a number: "))

result = 0
for i in range(0, n+1):
    result += i

print(result)