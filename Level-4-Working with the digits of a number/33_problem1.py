# Write a program to count the number of digits in a number n.

n = int(input("Enter a number: "))

count = 1 if n == 0 else 0

while n > 0:
    count += 1
    n //= 10

print(count)