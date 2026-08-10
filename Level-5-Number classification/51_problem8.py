# Write a program to check whether a number is an automorphic number.

n = int(input("Enter a number: ")) # 25

sq = n ** 2 # 625

while sq > 0: #
    digit = sq % 10 #

    sq //= 10 #

if n == digit:
    print("Yes, it's an automorphic number")
