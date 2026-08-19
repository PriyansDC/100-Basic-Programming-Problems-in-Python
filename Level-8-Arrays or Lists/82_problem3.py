# Write a program to find the largest and smallest element in an array.

arr = [1, 2, 3, 4, 5, 6, 7, 83, 32, 343, 23492, 343]

largest = arr[0]
smallest = arr[0]

for i in arr:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("The largest element in the array is: ", largest)
print("The smallest element in the array is: ", smallest)
