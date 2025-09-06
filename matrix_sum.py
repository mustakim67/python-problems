# adds two 2x2 matrices using nested loops.
matrix_a = [[1, 2],
            [3, 4]]

matrix_b = [[5, 6],
            [7, 8]]

result_matrix = [[0, 0],
                 [0, 0]]
7
for i in range(len(matrix_a)):
    for j in range(len(matrix_a[0])):
        result_matrix[i][j] = matrix_a[i][j] + matrix_b[i][j]

print("Matrix A:")
for row in matrix_a:
    print(row)

print("\nMatrix B:")
for row in matrix_b:
    print(row)

print("\nSum of the two matrices:")
for row in result_matrix:
    print(row)