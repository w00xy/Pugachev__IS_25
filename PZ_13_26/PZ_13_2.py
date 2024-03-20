import random

# В матрице элементы первого столбца возвести в куб.

matrix = [[random.randint(-2,4) for j in range(3)] for i in range(3)]

def cube_first_column(matrix):
    mx = [row[:] for row in matrix]

    for i in range(len(mx)):
        mx[i][0] = mx[i][0] ** 3

    for i, j in enumerate(mx):
        print(i, j)

    return


print('Исходная матрица: ', )
for i, j in enumerate(matrix):
    print(i, j)

print('\nГотовая матрица: ')
cube_first_column(matrix)