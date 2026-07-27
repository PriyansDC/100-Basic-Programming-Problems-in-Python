# Write a program to display the multiplication table of a number n.

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")