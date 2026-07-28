# Write a program to read three numbers and find the smallest among them.

a = 23
b = 3
c = 54

if a < b:
    if a < c:
        print("A is smallest")
    else:
        print("C is smallest")
elif b < c:
    print("B is smallest")
else:
    print("C is smallest")