import random
# В матрице найти среднее арифметическое положительных элементов

matrix = [[random.randint(-2,2) for j in range(3)] for i in range(3)]
# Вывод матрицы в удобном виде
# for i, j in enumerate(matrix):
#     print(i, j)


def sum_positive_integers(matrix):
    total_sum = 0
    for row in matrix:
        for num in row:
            if num > 0:
                total_sum += num
    return total_sum

print(f"Исходная матрица: {matrix}\n\nСумма положительных чисел в матрице: ", sum_positive_integers(matrix))