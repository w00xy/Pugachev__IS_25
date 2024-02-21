import random
from pprint import pprint


def generating_files():
    # Генерируем случайную последовательность чисел для первого файла
    sequence1 = [random.randint(-100, 100) for _ in range(10)]
    with open('file1.txt', 'w') as f1:
        f1.write(' '.join(map(str, sequence1)))

    # Генерируем случайную последовательность чисел для второго файла
    sequence2 = [random.randint(-100, 100) for _ in range(10)]
    with open('file2.txt', 'w') as f2:
        f2.write(' '.join(map(str, sequence2)))


def preprocessor():
    # Чтение последовательностей чисел из файлов
    with open('file1.txt', 'r') as f1:
        sequence1 = list(map(int, f1.read().split()))

    with open('file2.txt', 'r') as f2:
        sequence2 = list(map(int, f2.read().split()))

    result = []

    result.append(f"Элементы первого и второго файлов: {sequence1 + sequence2}")
    result.append(f"Элементы первого файла, отсутствующие во втором: {list(set(sequence1) - set(sequence2))}")
    result.append(f"Элементы второго файла, отсутствующие в первом: {list(set(sequence2) - set(sequence1))}")
    result.append(f"Количество элементов: {len(sequence1 + sequence2)}")
    result.append(f"Индекс первого минимального элемента: {sequence1.index(min(sequence1))}")
    result.append(f"Индекс последнего максимального элемента: {len(sequence1) + sequence2[::-1].index(max(sequence2))}")

    # Элементы первого и второго файлов
    print(f"Элементы первого и второго файлов: {sequence1 + sequence2}")

    # Элементы первого файла, отсутствующие во втором
    print(f"Элементы первого файла, отсутствующие во втором: {list(set(sequence1) - set(sequence2))}")

    # Элементы второго файла, отсутствующие в первом
    print(f"Элементы второго файла, отсутствующие в первом: {list(set(sequence2) - set(sequence1))}")

    # Количество элементов
    print(f"Количество элементов: {len(sequence1 + sequence2)}")

    # Индекс первого минимального элемента
    print(f"Индекс первого минимального элемента: {sequence1.index(min(sequence1))}")

    # Индекс последнего максимального элемента
    print(f"Индекс последнего максимального элемента: {len(sequence1) + sequence2[::-1].index(max(sequence2))}")


    # Запись результатов в новый файл
    with open('result.txt', 'w') as result_file:
        result_file.write('\n'.join(result))


generating_files()
preprocessor()
