# -*- coding: utf8 -*-
# Создать словарь и определить:
# 1. Полный список всех книг магазинов.
# 2. Какие книги есть во всех магазинах.
# 3. Хотя бы одну книгу, которая есть не во всех магазинах.

books = {
    'Magister': {'Lermontov', 'Dostoevskiy', 'Pushkin', 'Tutchev'},
    'DomKnigi': {'Tolstoy', 'Griboedov', 'Chehov', 'Pushkin'},
    'BookMarket': {'Pushkin', 'Dostoevskiy', 'Mayakovskiy'},
    'Gallery': {'Chehov', 'Tutchev', 'Pushkin'}
}

def all_books(slovar_knig):
    # all_books_list = []
    # for i in slovar_knig.values():
    #     for j in i:
    #         if j not in all_books_list:
    #             all_books_list.append(j)
    # return all_books_list

    all_books = set().union(*slovar_knig.values())
    return all_books

def can_buy_everywhere(slovar_knig):
    common_books = set.intersection(*slovar_knig.values())
    return common_books


def unique_book(slovar_knig):
    all_books = set().union(*slovar_knig.values())
    common_books = set.intersection(*slovar_knig.values())
    unique_book = all_books - common_books
    return unique_book


print(f'Список всех книг во всех магазинах - ', all_books(books))
print(f'Книги которые можно купить во всех магазинах - ', *can_buy_everywhere(books))
print(f'Книги которые можно купить НЕ во всех магазинах(уникальные) - ', unique_book(books))
