# Write a program to find the smallest digit in a number n.

n = int(input("Enter a number: "))

smallest = 0

while n > 0:
    digit = n % 10

    if digit < smallest:
        smallest = digit

    n //= 10