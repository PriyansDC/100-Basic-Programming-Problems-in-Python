# Write a program to read three numbers and find the largest among them.

a = 2300
b = 325
c = 54

if a > b:
    if a > c:
        print("A is greatest")
    else:
        print("C is greatest")
elif b > c:
    print("B is greatest")
else:
    print("C is greatest")