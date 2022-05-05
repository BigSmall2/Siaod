def sortDiag(matrix, i, s3=0, s4=0):
    diag = []
    s1 = s3
    s2 = s4
    while True:
        try:
            diag.append(matrix[s1][s2])
            s1 += 1
            s2 += 1
        except IndexError:
            break
    diag.sort()
    s1 = s3
    s2 = s4
    for j in range(len(diag)):
        matrix[s1][s2] = diag[j]
        s1 += 1
        s2 += 1

def sortDiagMatrix(matrix):
    for i in range(len(matrix)):  # сортирует верхние диагонали
        sortDiag(matrix, i, s3=i)
    for i in range(1, len(matrix[0])):  # сортирует нижние диагонали
        sortDiag(matrix, i, s4=i)
    return matrix

print("Matrix1: ")
arr = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
for l in arr:
    print(l)
print("\nSorted1: ")
arr = sortDiagMatrix([[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]])
for l in arr:
    print(l)

print("\nMatrix2: ")
arr = [[11, 25, 66, 1, 69, 7], [23, 55, 17, 45, 15, 52], [75, 31, 36, 44, 58, 8], [22, 27, 33, 25, 68, 4], [84, 28, 14, 11, 5, 50]]
for l in arr:
    print(l)
print("\nSorted2: ")
arr = sortDiagMatrix([[11, 25, 66, 1, 69, 7], [23, 55, 17, 45, 15, 52], [75, 31, 36, 44, 58, 8], [22, 27, 33, 25, 68, 4], [84, 28, 14, 11, 5, 50]])
for l in arr:
    print(l)