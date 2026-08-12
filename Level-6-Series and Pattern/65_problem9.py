# Write a program to print a pyramid pattern of stars of height n.

r = int(input("Enter the number of rows: "))

for i in range(1, r+1):

    for j in range(r - i):
        print(" ", end="")

    for j in range(i):
        print("*", end= " ")

    print()