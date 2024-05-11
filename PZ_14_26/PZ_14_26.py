import re

# В исходном текстовом файле(Dostoevsky.txt) найти все варианты фамилии
# Достоевского (т.е. с различными окончаниями, например, Достоевский,
# Достоевского) в единственном экземпляре.

with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    text = file.read()


variants = set(re.findall(r'\bДостоевск\w+(?<!ие)\b', text))


print(variants)

