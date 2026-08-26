# Exp-09: Remove Punctuations

import string

text = input("Enter a string: ")

result = ""

for char in text:
    if char not in string.punctuation:
        result += char

print("\nString after removing punctuations:")
print(result)