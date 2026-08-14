# Write a program to find the sum of the first and last digit of a number n.

n = int(input("Enter a number: "))

original = n
reverse = 0

first_digit = 0
last_digit = n % 10

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit

    n //= 10

first_digit = reverse % 10

print(f"The sum of the first and last digit of {original} is {first_digit + last_digit}")