# Write a program to count the number of even and odd elements in an array.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

count_odd = 0
count_even = 0

for i in arr:
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print(f"Even count: {count_even} \nOdd count: {count_odd}")