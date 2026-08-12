# Write a program to print Pascal's triangle for n rows.

r = int(input("Enter the number of rows: "))

sum = 0

for i in range(1, r+1):

    for j in range(r - i):
        print(" ", end="")

    for j in range(1, i+1):
      pass

    print()