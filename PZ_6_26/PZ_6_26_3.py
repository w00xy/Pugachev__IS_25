from itertools import combinations
from random import randint as ri
# -*- coding: utf8 -*-
#  ПЗ 6 вариант 26 задание 3
# Дано множество А из N точек (N> 2), точки заданы своими координатами (х, у). Найти
# такую точку из данного множества, сумма расстояний от которой до остальных его
# точек минимальна, и саму эту сумму.

# Задаем исходное множество точек A
A = [(ri(-10, 10), ri(-10, 10)) for i in range(0, ri(1, 10))]  # Пример входных данных, можно заменить на свои значения

# Функция для вычисления расстояния между двумя точками
def distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

# Создаем список всех возможных комбинаций точек для подсчета расстояний
point_combinations = list(combinations(A, 2))

# Инициализируем переменные для хранения наилучшей точки и наименьшей суммы расстояний
best_point = A[0]
min_distance_sum = float('inf')

# Цикл для вычисления сумм расстояний от каждой точки до остальных
for point in A:
    distance_sum = 0
    for other_point in A:
        if other_point != point:
            distance_sum += distance(point, other_point)
    if distance_sum < min_distance_sum:
        min_distance_sum = distance_sum
        best_point = point

# Выводим найденную точку и сумму расстояний
print(f"Все точки: {A}")
print("Наилучшая точка:", best_point)
print("Минимальная сумма расстояний:", min_distance_sum)
