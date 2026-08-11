# Write a program to find all factors (divisors) of a number n.

n = int(input("Enter a number: "))

for i in range(1, n+1):
    num = n % i
    if num == 0:
        print(i, end= ", ")