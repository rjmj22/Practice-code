# Write a Python program to concatenate all elements in a list into a string and return it.

def converter(items):
    string= ''
    for item in items:
        string += str(item)
    return string

print(converter([10, 25, 100]))