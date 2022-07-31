# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
num_one = int(input("Enter number: "))
num_two = int(input("Enter number: "))
num_three = int(input("Enter number: "))
if num_one == num_two or num_two == num_three or num_one == num_three:
    print("Sum = 0")
else:
    print(num_one + num_two + num_three)