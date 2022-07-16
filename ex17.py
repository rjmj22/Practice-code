# Write a Python program to test whether a number is within 100 of 1000 or 2000.
number = int(input("Enter number: "))
if number in range(900, 1100):
    print(number ,"is within 100 of 1000")
elif number in range(1900, 2100): 
    print(number ,"is within 100 of 2000")
else:
    print(number ,"is not within 100 of 1000 or 2000")