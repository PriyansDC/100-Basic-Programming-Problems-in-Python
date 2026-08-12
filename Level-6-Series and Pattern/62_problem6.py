# Write a program to find the value of x raised to the power y without using inbuilt power.

x = int(input("Enter a number: "))
y = int(input("Enter the power of the number: "))

result = 1

for i in range(1, y+1):
    result *= x

print(f"The value of {x} raised to the power {y} is: {result}")