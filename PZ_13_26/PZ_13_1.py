import random
from functools import reduce

# В матрице найти среднее арифметическое положительных элементов

matrix = [[random.randint(-2,2) for j in range(3)] for i in range(3)]
# Вывод матрицы в удобном виде
# for i, j in enumerate(matrix):
#     print(i, j)


def sum_positive_integers(matrix):
    total_sum = reduce(lambda acc, row: acc + sum(num for num in row if num > 0), matrix, 0)
    return total_sum / len([num for row in matrix for num in row if num > 0])

print(f"Исходная матрица: {matrix}\n\nСумма арифметичских чисел в матрице: ", sum_positive_integers(matrix))