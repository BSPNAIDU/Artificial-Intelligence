# Exp-02: Addition of Two Matrices

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements of Matrix A:")
A = []
for i in range(rows):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter elements of Matrix B:")
B = []
for i in range(rows):
    row = list(map(int, input().split()))
    B.append(row)

C = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("\nResultant Matrix:")
for row in C:
    print(row)