# Write a program to print a right-angled triangle pattern of stars of height n.

r = int(input("Enter the number of rows: "))

for i in range(1, r+1):
    
    for j in range(1, i+1):
        print("*", end= " ")

    print()