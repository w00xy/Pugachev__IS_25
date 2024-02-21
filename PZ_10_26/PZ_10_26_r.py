# -*- coding: utf8 -*-
# Создать словарь и определить:
# 1. Полный список всех книг магазинов.
# 2. Какие книги есть во всех магазинах.
# 3. Хотя бы одну книгу, которая есть не во всех магазинах.

magistr = {"Лермонтов", "Достоевский", "Пушкин", "Тютчев"}
domknigi = {"Толстой", "Грибоедов", "Чехов", "Пушкин"}
bookmarket = {"Пушкин", "Достоевский", "Маяковский"}
galery = {"Чехов", "Тютчев", "Пушкин"}


def all_books():

    all_books_set = magistr.union(domknigi, bookmarket, galery)
    return all_books_set


def can_buy_everywhere():
    common_books = magistr.intersection(domknigi, bookmarket, galery)
    return common_books


def unique_book():
    all_books_set = all_books()
    common_books = can_buy_everywhere()
    unique_book = all_books_set - common_books
    return unique_book


print(f'Список всех книг во всех магазинах - ', all_books())
print(f'Книги которые можно купить во всех магазинах - ', *can_buy_everywhere())
print(f'Книги которые можно купить НЕ во всех магазинах(уникальные) - ', unique_book())