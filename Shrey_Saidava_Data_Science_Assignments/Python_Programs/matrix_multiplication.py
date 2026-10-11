A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]
result = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        for k in range(3):
            result[i][j] += A[i][k] * B[k][j]
for row in result:
    print(row)
