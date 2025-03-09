# Igor Lab pickle.

import pickle  # подключить модуль.


class Book:
        def __init__(self):
                self.pages = []

        def add_page(self, text):
                self.pages.append(f"Page: {len(self.pages) + 1} - {text}")

        def __iter__(self):
                return iter(self.pages)


book = Book()  # Экземпляр book Класса Book.
for i in range(1,8):  # счетчик от 1 до 7.
        book.add_page(f"the page number is {i}")

for page in book:
        print(page)

print()
with open("data.pickle", "wb") as fo:
        pickle.dump(book, fo)

with open("data.pickle", "rb") as fo:  # пишем данные в файл data_new_book.
        data_new_book = pickle.load(fo)

for page in data_new_book:  # достаем данные и печатаем.
        print(page)
