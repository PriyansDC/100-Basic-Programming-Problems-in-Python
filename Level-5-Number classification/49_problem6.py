# Write a program to check whether a number is a perfect number.

n = int(input("Enter a number: "))

perfect_num = 0

for i in range(1, n):
    if n % i == 0:
        print(i, end= ", ")
        perfect_num += i

print(f"\nThe sum of the divisor of number {n} is {perfect_num}")
if perfect_num == n:
    print("It's a perfect number")
else:
    print("It's not a perfect number")