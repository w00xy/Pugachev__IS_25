import random
# -*- coding: utf8 -*-
#  ПЗ 6 вариант 26 задание 1
# Дан список ненулевых целых чисел размера N. Проверить, чередуется ли в нем положительные и отрицательные
# числа. Если чередуются то вывести 0, если нет, то вывести порядковый номер первого элемента нарушающего закономерность

# генерация списка ненулвых чисел
allowed_values = list(range(-5, 5+1))
allowed_values.remove(0)

# can be anything in {-5, ..., 5} \ {0}:
random_list = [random.choice(allowed_values) for i in range(1, random.randint(2, 5))]
# random_list = [-2,4,3]

# Функция с циклом для проверки созданного списка
def check_seq(rand_list):
    for i in range(0, len(rand_list)-1):
        if i % 2 == 0:
            if rand_list[i] > 0 and rand_list[i+1] < 0 or rand_list[i] < 0 and rand_list[i + 1] > 0:
                continue
            else:
                return rand_list[i+1]
        else:
            if rand_list[i] < 0 and rand_list[i + 1] > 0 or rand_list[i] > 0 and rand_list[i+1] < 0:
                continue
            else:
                return rand_list[i+1]
    return 0

# Выводы
print(f"[INFO] {random_list}")
print(check_seq(rand_list=random_list))