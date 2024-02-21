# В последовательности их N чисел (N –четное) во второй ее половине найти сумму
# элементов больших 10.

def sum_elements_greater_than_10(sequence):
    mid = len(sequence) // 2
    second_half = sequence[mid:]
    filtered_elements = filter(lambda x: x > 10, second_half)
    sum_of_elements = sum(filtered_elements)
    return sum_of_elements

sequence = [5, 12, 3, 8, 20, 15, 10, 25, 7, 30]  # пример последовательности чисел
N = len(sequence) # количество элементов в последовательности

if len(sequence) % 2 == 0:  # проверка на четность числа N
    result = sum_elements_greater_than_10(sequence)
    print("Сумма элементов больше 10 во второй половине последовательности:", result)
else:
    print("Число элементов в последовательности должно быть четным.")