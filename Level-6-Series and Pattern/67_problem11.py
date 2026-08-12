# Write a program to print Pascal's triangle for n rows.

r = int(input("Enter the number of rows: "))

previous = 0

for i in range(1, r+1):

    for j in range(r - i):
        print(" ", end="")

    for j in range(1, i+1):
        if j == 1 or j == i:
            current = 1
        else:
            current = previous * (i - j + 1) // (j - 1)

        print(current, end=" ")
        previous = current

    print()