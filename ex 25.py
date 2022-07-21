#  Write a Python program to check whether a specified value is contained in a group of values.
given_data = [1, 5, 8, 3]
get_number = int(input("Enter single digit number: "))
if get_number in given_data:
    print(get_number, "is in data")
else:
    print(get_number, "is not in data")