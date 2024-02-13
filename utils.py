FILE_CSV = 'Phonebook.csv'


def input_data():
    """ Функция ввода/обновления данных в телефонном справочнике.
    """
    data = []
    flag = False
    last_name = input('Введите Фамилию: ')
    data.append(last_name)
    first_name = input('Введите Имя: ')
    data.append(first_name)
    middle_name = input('Введите Отчество: ')
    data.append(middle_name)
    organization = input('Введите наименование Организации: ')
    data.append(organization)

    while not flag:
        try:
            work_phone = input('Введите Рабочий телефон: ')
            home_phone = input('Введите Домашний телефон: ')
            if len(work_phone) != 11 or len(home_phone) != 11:
                print('В номере телефона должно быть 11 цифр!')
            else:
                work_phone = int(work_phone)
                data.append(work_phone)
                home_phone = int(home_phone)
                data.append(home_phone)
                flag = True
        except Exception as e:
            print('Номер телефона не должен содержать букв!!!')
            print(e)
    return data


def read_book():
    """ Чтение телефонного справочника.
    """
    with open(FILE_CSV, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines


def write_book():
    """ Запись данных в телефонный справочник.
    """
    data = input_data()

    with open(FILE_CSV, 'a', encoding='utf-8') as file:
        file.write(f'{data[0]};{data[1]};{data[2]};{data[3]};{data[4]};{data[5]}\n')


def search_in_book():
    """ Поиск записей в телефонном справочнике.
    """
    search = input('Введите поисковый запрос (Иван Иванов или Иван Телепузики, например :) )\n').lower().split()
    number = 0
    lines = read_book()
    for line in lines:
        number += 1
        count = 0
        for word in search:
            if word in ''.join(line).replace(';', ' ').lower():
                count += 1
        if count == len(search):
            print(f'{number}: {line}')



def record_change():
    """ Внесение изменений в запись справочника.
    """
    search_in_book()
    record = int(input('Введите строку для редактирования '))

    data = input_data()

    lines = read_book()
    lines[record - 1] = f'{data[0]};{data[1]};{data[2]};{data[3]};{data[4]};{data[5]}\n'

    with open(FILE_CSV, 'w', encoding='utf-8') as file:
        file.writelines(lines)
    print('Запись успешно изменена')
