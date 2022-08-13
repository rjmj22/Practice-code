# Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.
numbers = list(range(1,50))
third_number = []
for i in range(1, len(numbers), 3):
    third_number.append([i])
print(third_number)
