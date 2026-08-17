# Write a program to read n elements into an array and print them.

n = int(input("How much size do you want of an array: "))

arr = []

for i in range(1, n+1):
    arr.append(input("Enter the element of the array: "))

print(arr)