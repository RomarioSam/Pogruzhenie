# Напишите функцию для транспонирования матрицы
# Пример:
# [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

MATRIX = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def trans(matrix):
    new_matrix = []
    for i in zip(*matrix):
        new_matrix.append(list(i))
    return new_matrix


print(trans(MATRIX))
