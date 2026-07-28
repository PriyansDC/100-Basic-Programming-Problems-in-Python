# Write a program to find the product of all natural numbers from 1 to n (factorial of n).

n = int(input("Enter a number: "))

result = 1

for i in range(1, n+1):
    result *= i

print(f"Factorial of {n}: {result}")