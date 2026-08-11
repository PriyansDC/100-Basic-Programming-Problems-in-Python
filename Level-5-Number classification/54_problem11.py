# Write a program to count the number of factors of a number n.

n = int(input("Enter a number: "))

count = 0

for i in range(1, n+1):
    num = n % i
    if num == 0:
        print(i, end= ", ")
        count += 1

print(f"\nThe number of factors of number {n} is {count}")