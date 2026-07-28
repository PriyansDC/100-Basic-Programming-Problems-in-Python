# Write a program to count the number of even digits and odd digits in a number n.

n = int(input("Enter a number: "))

even_count = 0
odd_count = 0

while n > 0:
    digit = n % 10

    if digit % 2 == 0:
        if digit != 0:
            even_count += 1
    else:
        odd_count += 1

    n //=10

print(f"The total number of even number is: \nEven no: {even_count} \nOdd no: {odd_count}")