# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
num_one = int(input("Enter number: "))
num_two = int(input("Enter number: "))
total = num_one + num_two
if total in range(15, 20):
    print("Answer is 20")
else:
    print(total)