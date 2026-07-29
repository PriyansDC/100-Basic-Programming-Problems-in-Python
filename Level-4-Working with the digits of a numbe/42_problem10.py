# Write a program to replace all zeros in a number n with the digit 5.

n = int(input("Enter a number: "))

reverse = 0
new_num = 0

while n > 0:
    digit = n % 10

    if digit == 0:
        digit = 5

    reverse = reverse * 10 + digit

    n //= 10

while reverse > 0:
    digit = reverse % 10
    new_num = new_num * 10 + digit

    reverse //= 10

print(new_num)