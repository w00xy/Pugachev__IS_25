#  Создайте класс "Человек", который содержит информацию о имени, возрасте и поле.
# Создайте классы "Мужчина" и "Женщина", которые наследуются от класса
# "Человек". Каждый класс должен иметь метод, который выводит информацию о
# поле объекта.

class Person():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def get_sex(self):
        return f"Gender: {self.sex}"


class Man(Person):
    def __init__(self, name, age):
        super().__init__(name, age, "Male")


class Woman(Person):
    def __init__(self, name, age):
        super().__init__(name, age, 'Female')


man = Man("John", 30)
female = Woman('Irina', 20)


print(man.get_sex())
print(female.get_sex())


