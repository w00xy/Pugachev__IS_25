# Создайте класс «Круг», который имеет атрибут радиуса и методы для вычисления
# площади, длины окружности и диаметра.

class Circle():
    """
    A simple class for creating circle and counting sqyare of cirlce, cirmunference and diametr.
    """

    def __init__(self, radius: int):
        self.radius = radius

    def square(self,):
        return round(3.14159 * self.radius ** 2, 2)

    def circumference(self):
        return round(3.14159 * 2 * self.radius, 2)

    def diameter(self):
        return 2 * self.radius


circle1 = Circle(3)
circle2 = Circle(5)

# square of circles
s1_s = circle1.square()
s2_s = circle2.square()

# circumference of circles
s1_c = circle1.circumference()
s2_c = circle2.circumference()

# diametr of circles
s1_d = circle1.diameter()
s2_d = circle2.diameter()

if __name__ == '__main__':
    # some outputs
    print(f'Площадь первого круга: {s1_s}\nПлощадь второго круга: {s2_s}\n{'-'*40}')

    print(f'Длина окружности первого круга: {s1_c}\nДлина окружности второго круга: {s2_c}\n{'-'*40}')

    print(f'Диаметр первого круга: {s1_d}\nДиаметр второго круга: {s2_d}')
