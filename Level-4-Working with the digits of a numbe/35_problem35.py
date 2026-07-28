# Write a program to find the sum of all digits of a number n.

n = int(input("Enter a number: "))

sum = 0

for i in range(len(str(n))):
    digit = n % 10
    sum += digit
    n //= 10

print(sum)