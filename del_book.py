FILE_CSV = 'Phonebook.csv'


def del_phonebook():
    """ Функция автоматического создания записей телефонного справочника.
    """
    with open(FILE_CSV, 'w', encoding='utf-8') as file:
        file.write(f'')


del_book = del_phonebook()
