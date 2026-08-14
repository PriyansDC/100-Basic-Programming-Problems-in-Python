# Write a program to check whether a number n is a palindrome (reads the same reversed).

n = int(input("Enter a number: "))

original = n
reverse = 0

while n > 0:
    digit = n % 10 
    reverse = reverse * 10 + digit
    n //= 10

if original == reverse:
    print(f"Yes your given number {reverse} is a palindrome number.")
else:
    print(f"No, it's not a palindrome number")