# Write a Python program to create the combinations of 3 digit combo.
from itertools import permutations
numbers = permutations([3, 5, 7], 3)
for i in numbers:
    print(i)
