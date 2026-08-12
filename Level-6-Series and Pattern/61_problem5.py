# Write a program to find the sum of the series 1 + 1/2 + 1/3 + ... + 1/n.

n = int(input("Enter a number: "))

result = 0
frac = 0

for i in range(1, n+1):
    frac = 1/i
    result += frac

print(f"The sum of the series 1 + 1/2 + 1/3 + ... + 1/{n} is: {result}")