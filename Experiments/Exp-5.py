# Exp-05: List Operations

numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

# Nested List
nested_list = [1, 2, [3, 4], [5, 6]]
print("Nested List:", nested_list)

# Length
print("Length:", len(numbers))

# Concatenation
list2 = [60, 70]
print("Concatenation:", numbers + list2)

# Membership
print("Is 30 present?", 30 in numbers)
print("Is 100 present?", 100 in numbers)

# Iteration
print("\nIteration:")
for item in numbers:
    print(item)

# Indexing
print("\nIndexing:")
print("First element:", numbers[0])
print("Third element:", numbers[2])

# Slicing
print("\nSlicing:")
print("First three elements:", numbers[:3])
print("Last two elements:", numbers[-2:])