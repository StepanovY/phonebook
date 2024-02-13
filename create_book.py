import random

FILE_CSV = 'Phonebook.csv'
list_organization = ['Один', 'Рога и копыта', 'Телепузики', 'Автопрокат', 'МБСОШ39']


def create_phone():
    phone = random.randrange(80000000001, 89999999999)
    return phone


def create_phonebook():
    """ Функция автоматического создания записей телефонного справочника.
    """
    with open(FILE_CSV, 'w', encoding='utf-8') as file:
        file.write(f'Фамилия;Имя;Отчество;Организация;Рабочий телефон;Домашний телефон\n')

    for i in range(100):
        organization = random.choice(list_organization)
        # phone = random.randrange(80000000001, 89999999999)
        with open(FILE_CSV, 'a', encoding='utf-8') as file:
            file.write(f'Last_name{i};First_name{i};Middle_name{i};{organization};'
                       f'{create_phone()};{create_phone()}\n')


phonebook = create_phonebook()
