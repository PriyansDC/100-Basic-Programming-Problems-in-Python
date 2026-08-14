# Write a program to find the product of all digits of a number n

n = int(input("Enter a number: "))

mul = 1

for i in range(len(str(n))):
    digit = n % 10
    mul *= digit
    n //= 10

print(mul)