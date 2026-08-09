# Write a program to check whether a number is a strong number (sum of factorials of its digits).

n = int(input("Enter a number: "))

original = n  # used this to compare the result and to improve the output message, so that we can print the original number instead of 0 at the end.
fact_sum = 0

while n > 0:
    digit = n % 10
    fact = 1

    for i in range(1, digit+1):
        fact *= i

    fact_sum += fact 

    n //= 10

if fact_sum == original:
    print(f"Yes, your number {original} is a strong number (sum of factorials of its digits).")
else:
    print(f"Nope, your given number {original} is not a strong number.")
