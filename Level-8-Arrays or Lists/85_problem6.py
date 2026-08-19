# Write a program to reverse the elements of an array.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

rev_arr = []

for i in range(len(arr)-1, -1, -1):
    rev_arr.append(arr[i])

print(f"Reversed array: {rev_arr}")