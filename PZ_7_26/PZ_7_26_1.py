import random
# -*- coding: utf8 -*-
#  ПЗ 7 вариант 26 задание 1
# Даны целые положительные числа N1 и N2 и строки S1 и S2. Получить из этих строк
# новую строку, содержащую первые N1 символов строки S1 и последние N2
# символов строки S2 (в указанном порядке).

def combine_strings(N1, N2, S1, S2):
    result = S1[:N1] + S2[-N2:]
    return result

N1 = random.randint(1,5)
N2 = random.randint(1,5)
S1 = ''.join([random.choice('abcdf123') for i in range(10)])
S2 = ''.join([random.choice('qwerty456') for i in range(10)])

new_string = combine_strings(N1, N2, S1, S2)

# Выводы
print(f'[INFO] N1 = {N1} | N2 = {N2}')
print(f'[INFO] S1 = {S1} | S2 = {S2}')
print(new_string)