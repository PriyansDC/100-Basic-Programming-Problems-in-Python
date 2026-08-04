# Write a program to check whether a number is an Armstrong number.

n = int(input("Enter a number: "))

original = n
temp = n
num = 0
count = 0

while temp > 0:
    count += 1
    temp //= 10

while n > 0:
    digit = n % 10
    num += digit ** count

    n //= 10
    
if original == num:
    print("Yes, it's an armstrong number")
else:
    print("Oops! It's not an armstrong number")