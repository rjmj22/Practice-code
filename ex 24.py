# Write a Python program to test whether a passed letter is a vowel or not.
letter = str(input("Enter letter: "))
small_letter = letter.lower()
vowel = ['a', 'e', 'i', 'o', 'u']
if small_letter in vowel:
    print("letter is a vowel")
else:
    print("letter is not a vowel")