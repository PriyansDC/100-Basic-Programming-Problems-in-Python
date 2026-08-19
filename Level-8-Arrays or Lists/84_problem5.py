# Write a program to search for an element in an array (linear search).

n = int(input("Enter a number: "))

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 23, 343, 33, 45, 32, 453, 221]

for i in range(len(arr)):
    if arr[i] == n:
        print(f"Number {arr[i]} found at {i}\n")
        break
else:
    print("The number you've entered is not present in the array.")

# enumerate
for index, i in enumerate(arr):
    print(f"{i} at index {index}")