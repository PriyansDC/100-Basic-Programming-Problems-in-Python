# Write a program to display the first n prime numbers.

n = int(input("Enter the number of prime numbers: "))

current_number = 2
prime_count = 0

while prime_count < n:
    isPrime = True

    for i in range(2, current_number):
        if current_number % i == 0:
            isPrime = False
            break

    if isPrime:
        print(current_number)
        prime_count += 1

    current_number += 1