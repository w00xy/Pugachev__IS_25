import random
# -*- coding: utf8 -*-
#  ПЗ 7 вариант 26 задание 2
# Даны строки S и S0. Удалить из строки S все подстроки, совпадающие с S0. Если
# совпадающих подстрок нет, то вывести строку S без изменений.

def remove_substrings(S, S0):
    return S.replace(S0, '')

S = ''.join([random.choice('abc123') if i != 5 else random.choice('ABC') for i in range(10)])
S0 = ''.join([random.choice('abc123') if i != 5 else random.choice('ABC') for i in range(2)])
result = remove_substrings(S, S0)

if not S0 in S:
    print(f'[INFO] Подстроки {S0} нет в {S}\n\n{S}')
else:
    print(f'[INFO] Подстрака {S0} найдено в {S} и была удалена из строки\n\n{result}')
