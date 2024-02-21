# -*- encoding: utf-8 -*-
# Чтение содержимого текстового файла
with open('text18-26.txt', 'r') as text_file:
    text = text_file.read()

# Подсчет количества знаков препинания
punctuation_count = sum(1 for char in text if char in '.,?!:;-—')

# Замена знаков пунктуации на '/'
text_with_slash = ''.join(['/' if char in '.,?!:;-—' else char for char in text])

# Вывод информации на экран
print("Содержимое текстового файла:")
print(text)
print("Количество знаков препинания:", punctuation_count)

# Запись текста с заменой пунктуации в новый файл
with open('poem.txt', 'w') as poem_file:
    poem_file.write(text_with_slash)
