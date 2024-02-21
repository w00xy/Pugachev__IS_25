# Составить генератор (yield), который выводит из строки только буквы.

def letters_generator(input_string):
    for char in input_string:
        if char.isalpha():
            yield char

# Пример использования генератора
input_string = "Пример строки с 123 цифрами и буквами ABC"
letters = letters_generator(input_string)

# Выводим буквенные символы из строки
for letter in letters:
    print(letter, end='')
