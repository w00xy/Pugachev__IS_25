import random

# В матрице элементы первого столбца возвести в куб.

matrix = [[random.randint(-2,4) for j in range(3)] for i in range(3)]

def cube_first_column(matrix):
    return [[row[0] ** 3 if idx == 0 else row[idx] for idx in range(len(row))] for row in matrix]


print('Исходная матрица: ', )
for i, j in enumerate(matrix):
    print(i, j)

print('\nГотовая матрица: ')
print(cube_first_column(matrix))