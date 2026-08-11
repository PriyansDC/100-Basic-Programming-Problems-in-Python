# Write a program to check whether a number is an automorphic number.

# Take a number as input
#         ↓
# Store the original number
#         ↓
# Count the number of digits
#         ↓
# Calculate the square
#         ↓
# Extract the last "count" digits from the square
#         ↓
# Compare those digits with the original number
#         ↓
# If they match → Automorphic

n = int(input("Enter a number: "))

count = len(str(n))
intCount = int(count)

sq = n ** 2

last_digits = sq % (10 ** count)

if last_digits == n:
    print("Yes, it's an automorphic number")
else:
    print("No, it's not an automorphic number")

