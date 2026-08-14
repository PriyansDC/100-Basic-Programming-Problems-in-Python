# Write a program to display all the digits of a number n (one per line).

# n = int(input("Enter a number: "))
# rev = 0

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n //= 10

# while rev > 0:
#     print(rev % 10)
#     rev //= 10

n = input("Enter a number: ")

for i in range(len(n)):
    print(n[i])
