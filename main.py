from utils import read_book, search_in_book, write_book, record_change


def main():
    """ Основной модуль работы с программой.
    """
    print('Вас приветствует телефонный справочник\n')
    while True:
        print(
            'Что Вы хотите сделать?:\n'
            '1. Прочитать весь телефонный справочник.\n'
            '2. Выполнить поиск.\n'
            '3. Добавить запись в справочник.\n'
            '4. Изменить запись в справочнике.\n'
            'Выберите пункт или нажмите любую кнопку для выхода \n'
        )
        action = input('')
        if action.isdigit():
            if int(action) == 1:
                count_lines = int(input('Введите количество строк для постраничного вывода справочника: '))
                lines = read_book()
                for i in range(1, len(lines), count_lines):
                    print(''.join(lines[0]).replace(';', ' || '))
                    print(''.join(lines[i:i + count_lines]).replace(';', ' || '))
                    step = input('Нажмите "Enter" для продолжения или "Q" для завершения чтения справочника \n')
                    if step == '':
                        continue
                    else:
                        break
            if int(action) == 2:
                search_in_book()
                print('Поиск завершен')
            if int(action) == 3:
                write_book()
            if int(action) == 4:
                record_change()
        else:
            print('Работа со справочником завершена')
            break


if __name__ == '__main__':
    main()
