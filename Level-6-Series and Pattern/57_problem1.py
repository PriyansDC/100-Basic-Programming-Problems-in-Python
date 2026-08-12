# Write a program to display the first n terms of the Fibonacci series.

n = int(input("Enter a number: "))

a = 0
b = 1

for i in range(1, n+1):
    c = a + b

    print(f"{a} + {b} = {c}")
    
    a = b
    b = c