from random import randint as ri
# -*- coding: utf8 -*-

#  ПЗ 6 вариант 26 задание 2
# Дан целочисленный список A размера N < 15. Переписать в новый целочисленный список B все элементы с нечетными
# порядковыми номерами (1,3,5) и вывести размер полученного списка B и его содержимое. Условный оператор не использовать

A = [ri(1, 100) for i in range(0, ri(1,15))]
B = A[1::2]

print(f"[INFO] начальный список: {A}\n")
print(f"[INFO] полученный список B с нечетными индексами: {B}\n\n[INFO] размер полученного списка B: {len(B)}")