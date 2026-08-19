# Write a program to find the second largest element in an array.

arr = [1, 2, 3, 4, 5, 6, 7, 83, 32, 343, 23492, 343]

largest = arr[0]
second_largest = arr[0]

for i in arr:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print("The second largest element in the array is: ", second_largest)