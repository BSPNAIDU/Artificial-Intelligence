# Exp-07: Set Operations

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Set A:", A)
print("Set B:", B)

# Union
print("\nUnion:", A | B)

# Intersection
print("Intersection:", A & B)

# Difference
print("A - B:", A - B)

# Difference
print("B - A:", B - A)

# Symmetric Difference
print("Symmetric Difference:", A ^ B)

# Subset
print("Is A subset of B?", A.issubset(B))

# Superset
print("Is A superset of B?", A.issuperset(B))