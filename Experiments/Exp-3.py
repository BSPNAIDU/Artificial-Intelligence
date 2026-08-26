# Exp-03: Transpose of a Matrix

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter matrix elements:")

matrix = []

for i in range(rows):
    matrix.append(list(map(int, input().split())))

print("\nOriginal Matrix:")
for row in matrix:
    print(row)

transpose = []

for j in range(cols):
    row = []
    for i in range(rows):
        row.append(matrix[i][j])
    transpose.append(row)

print("\nTranspose Matrix:")
for row in transpose:
    print(row)