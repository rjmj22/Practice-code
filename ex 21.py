# Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
number = int(input("Enter number: "))
last_number = number % 10
if number%2 == 0:
    print(number , "is even")
else:
    print(number , "is odd")
