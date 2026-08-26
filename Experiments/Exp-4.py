# Exp-04: Sort Sentence in Alphabetical Order

sentence = input("Enter a sentence: ")

words = sentence.split()

words.sort()

print("\nWords in alphabetical order:")

for word in words:
    print(word)