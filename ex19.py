# Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
string = input("Enter string here: ")
if string.startswith(('is', 'Is')):
    print(string)
else:
    string = 'Is ' + string
    print(string)