# Write a program to find the sum and average of all elements in an array.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = 0

for i in arr:
    sum += i

avg = sum / len(arr)

print(f"Sum: {sum} \nAverage: {avg}")