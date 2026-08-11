# Write a program to check whether a number is a Harshad (Niven) number.

n = int(input("Enter a number: "))

original = n
sum = 0

while n > 0:
    digit = n % 10
    sum += digit

    n //= 10

if original % sum == 0:
    print("Yes, it's a Harshad (Niven) number.")
else:
    print("No, it's not a Harshad (Niven) number")