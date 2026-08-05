# Write a program to display all Armstrong numbers from 1 to n.

n = int(input("Enter a number: "))

for i in range(1, n+1):

    num = 0
    count = 0
    temp = i

    while temp > 0:
        count += 1
        temp //= 10

    temp = i

    while temp > 0:
        digit = temp % 10
        num += digit ** count
        temp //= 10

    if i == num:
        print(num, end= ", ")
