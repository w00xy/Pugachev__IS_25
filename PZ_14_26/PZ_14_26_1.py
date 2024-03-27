import re
# В исходном текстовом файле(Dostoevsky.txt) найти все варианты фамилии
# Достоевского (т.е. с различными окончаниями, например, Достоевский,
# Достоевского) в единственном экземпляре. 


with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    text = file.read()

surname_occurrences = re.findall(r'\bДостоевск\w+', text)
unique_surnames = set(surname_occurrences)

print(f'количество совпадений: {len(unique_surnames)}')

for surname in unique_surnames:
    print(surname)

