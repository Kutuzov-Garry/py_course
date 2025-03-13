# main CSV phonebook.

from lab_phonebook import Phone
"""импорт, вывод, поиск, экспорт контактов
телефонной книги"""


phone = Phone()
phone.import_contacts_from_csv("contacts.csv")
phone.show()
phone.search_contacts()
phone.export_contacts_to_csv("exported_contacts.csv")


# _projects\py_course\Lecture14\phonebook\main.py
# Импортирую контакты.
# Импорт был успешен...
# Список контактов:
# Contact: Name:Phone
# Contact: mother:222-555-101
# Contact: father:222-555-102
# Contact: wife:222-555-103
# Contact: mother-in-law:222-555-104
# Поиск контактов: mother
# Поиск контакта по фразе.
# Найден контакт: mother 222-555-101
# Найден контакт: mother-in-law 222-555-104
# Экспортирую контакты.
# Экспорт был успешен...
