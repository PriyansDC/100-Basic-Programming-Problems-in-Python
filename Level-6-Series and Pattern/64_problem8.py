# Write a program to print an inverted right-angled triangle pattern of stars of height n.

r = int(input("Enter the number of rows: "))

i = r

for i in range(r, 0, -1):

    for j in range(1, i+1):
        print("*", end= " ")

    print()