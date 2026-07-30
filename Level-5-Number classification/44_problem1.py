# Write a program to read a number and check whether it is prime or not.

n = int(input("Enter a number: "))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(n, "is not a Prime number.")
            break
    else:
        print(n, "is a Prime number")
else:
    print("Number should be greater than 1")

# A better way to solve this is:

if n > 1:
    for i in range(2, int(n ** 0.5) + 1):
        if n % 1 == 0:
            print(n, "is not a Prime number.")
            break
    else:
        print(n, "is a Prime number")

else:
    print("Number should be greater than 1")