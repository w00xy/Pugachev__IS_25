# В последовательности их N чисел (N –четное) во второй ее половине найти сумму
# элементов больших 10.
import random

def sum_elements_greater_than_10(sequence):
    return sum([x for x in sequence[len(sequence) // 2:] if x > 10])


sequence = [random.randint(-1, 12) for i in range(10)]  # пример последовательности чисел
N = len(sequence) # количество элементов в последовательности
print(f'{sequence} - сгенерированный список')
if len(sequence) % 2 == 0:  # проверка на четность числа N
    result = sum_elements_greater_than_10(sequence)
    print("Сумма элементов больше 10 во второй половине последовательности:", result)
else:
    print("Число элементов в последовательности должно быть четным.")