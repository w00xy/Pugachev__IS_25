# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
# сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в
# бинарном формате.

import pickle

from PZ_16_26.PZ_16_26_1 import Circle


# Функция для сохранения информации экземпляра класса в файл
def save_def(*args):
    with open('circle_info.pkl', 'wb') as file:
        pickle.dump(args, file)


# Функция для загрузки информации экземпляра класса из файла
def load_def(file_name):
    with open(file_name, 'rb') as file:
        data = pickle.load(file)
        return data


circle1 = Circle(3)
circle2 = Circle(5)

# Сохранение информации об экземплярах класса в файл
save_def(circle1, circle2)

# Загрузка информации об экземплярах класса из файла
loaded_circles = load_def('circle_info.pkl')


# Вывод информации о диаметре первого круга до и после сохранения и загрузки
print(f'Диаметр первого круга до загрузки: {circle1.diameter()}')
print(f'Диаметр первого круга после загрузки: {loaded_circles[0].diameter()}\n')

print(f'Диаметр первого круга до загрузки: {circle2.diameter()}')
print(f'Диаметр первого круга после загрузки: {loaded_circles[1].diameter()}')
