
phone_book = {}

path: str = 'Phones.txt'
def open_file():
    phone_book.clear()
    file = open(path, 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    for contact in data:
        nc = contact.strip().split(':')
        phone_book[int(nc[0])] = {'name': nc[1], 'phone': nc[2], 'comment': nc[3]}
    print('\nТелефонная книга загружена!')

def save_file():
    data = []
    for i, contact in phone_book.items():
        new = ':'.join([str(i), contact.get('name'), contact.get('phone'), contact.get('comment')])
        data.append(new)
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)
    print(f'\nТелефонная книга успешно сохранена!')
    print('=' * 200 + '\n')

def show_contacs(book: dict[int, dict]):
    print('\n' + '=' * 200)
    for i, cnt in book.items():
        print(f'{i:>3}. {cnt.get("name"):<20}{cnt.get("phone"):<20}{cnt.get("comment"):<20}')
    print('=' * 200 + '\n')

def menu() -> int:
    main_menu = '''Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход'''
    print(main_menu)

    while True:
        select = input('Введите пункт меню: ')
        if select.isdigit() and 0 < int(select) < 9:
            return int(select)
        print('Ошибка ввода, введите ЧИСЛО от 1 до 8!!!')

def search():
    result = {}
    word = input('Ищем: ')
    for i, contact in phone_book.items():
        if word.lower() in ' '.join(list(contact.values())).lower():
            result[i] = contact
    return result

def change_contakt():
    result = search()
    show_contacs(result)
    index = int(input('Введите ID для изменения: '))

    while True:
        select = input('Какое поле редактировать? (имя, телефон, комментарий): \nили exit для выхода в предыдущее меню')
        if select.isdigit():
            print('Введите название поля, а не число!')
        elif (select.lower() == 'имя' or
              select.lower() == 'телефон' or
              select.lower() == 'комментарий' or
              select.lower() == 'exit'):
            match select:
                case 'имя':
                    phone_book[index]['name'] = input('Введите новое имя: ')
                    print('\nКонтакт успешно изменен!')
                    show_contacs(result)
                case 'телефон':
                    phone_book[index]['phone'] = input('Введите новый номер: ')
                    print('\nКонтакт успешно изменен!')
                    show_contacs(result)
                case 'комментарий':
                    phone_book[index]['comment'] = input('Введите новый комментарий: ')
                    print('\nКонтакт успешно изменен!')
                    show_contacs(result)
                case 'exit':
                    break
        else:
            print('Такого поля нет!!!')


def delete_contack():
    result = search()
    show_contacs(result)
    index = int(input('Введите ID для удаления: '))
    del_cnt = phone_book.pop(index)
    print(f'Контакт {del_cnt} успешно удален!')
    print('=' * 200 + '\n')

def add_contact():
    uid = max(list(phone_book.keys())) + 1
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий: ')
    phone_book[uid] = {'name': name, 'phone': phone, 'comment': comment}
    print(f'\nКонтакт {name} успешно добавлен!')
    print('=' * 200 + '\n')

open_file()
while True:
    select = menu()
    match select:
        case 1:
            open_file()
        case 2:
            save_file()
        case 3:
            show_contacs(phone_book)
        case 4:
            add_contact()
        case 5:
            result = search()
            show_contacs(result)
        case 6:
            change_contakt()
        case 7:
            delete_contack()
        case 8:
            print('До скорой встречи!')
            break







