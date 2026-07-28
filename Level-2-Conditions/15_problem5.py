# Write a program to read a year and check whether it is a leap year or not.

year = 20010

if year % 4 == 0:
    print("leap year")
elif year % 4 != 0:
    print("not a leap year")
else:
    print("Invalid")