# Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum
num1 = int(input("Enter number one: "))
num2 = int(input("Enter number one: "))
num3 = int(input("Enter number one: "))
if num1 == num2:
    if num2 == num3:
        print(((num1 + num2 + num3) * 3), "is the total")
else:
    print((num1 + num2 + num3), "is the total")