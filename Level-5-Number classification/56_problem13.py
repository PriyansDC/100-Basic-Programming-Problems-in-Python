# Write a program to find the LCM of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

is_lcm = True
i = 1

while is_lcm:
    if (a * i) % b == 0:
        print("LCM:", a * i)
        is_lcm = False

    i += 1

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# for i in range(1, b + 1):
#     if (a * i) % b == 0:
#         print("LCM:", a * i)
#         break