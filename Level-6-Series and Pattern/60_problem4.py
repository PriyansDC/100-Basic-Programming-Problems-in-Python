# Write a program to find the sum of the series 1^2 + 2^2 + 3^2 + ... + n^2.

n = int(input("Enter a number: "))

result = 0
sq = 0

for i in range(1, n+1):
    sq = i ** 2
    result += sq

print(f"The sum of square of first n natural number is: {result}")