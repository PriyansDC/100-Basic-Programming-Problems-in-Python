# Write a program to display all multiples of a number m up to n terms.

m = int(input("Enter a number: "))
n = int(input("How many multiples do you want: "))

print(f"Multiples of {m}:")
for i in range(1, n+1):
    print(m*i, end= ", ")