# Напишите функцию для транспонирования матрицы
matrix = [[1,2,3], [4,5,6]]


def matrix_transpon(marix: list) -> list:
    new_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix

print(matrix_transpon(matrix))        