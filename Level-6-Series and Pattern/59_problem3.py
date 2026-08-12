# Write a program to find the sum of the series 1 + 2 + 3 + ... + n.

n = int(input("Enter a number: "))

result = 0

for i in range(1, n+1):
    result += i

print(f"The sum of first n natural numbers is: {result}")