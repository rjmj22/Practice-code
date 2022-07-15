# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
number_input = int(input("Insert number: "))
if number_input <= 17:
    output = 17 - number_input 
else:
    output = ((number_input - 17) * 2)
print(output)