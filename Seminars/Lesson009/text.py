main_menu = ['Главное меню',
             'Открыть файл',
             'Сохранить файл',
             'Показать все контакты',
             'Добавить контакт',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Выход']

select_menu = 'Выберите пункт меню: '
input_error = f'Ошибка ввода. Введите число от 1 до {len(main_menu) - 1}'

new_contact = {'name': 'Введите имя контакта: ',
               'phone': 'Введите телефон: ',
               'comment': 'Введите комментарий: '}

load_successful = 'Телефонная книга успешно загружена!'
save_successful = 'Телефонная книга успешно сохранена!'
error_load = 'Телефонная книга не загружена!'
error_save = 'Телефонная книга не сохранена!'
empty_book = 'Телефонная книга пуста или не открыта!'
search_word = 'Введите слово для поиска: '

index_delete = 'Введите индекс для удаления: '
index_change = 'Введите индекс для изменения: '
change_fld = 'Какое поле редактировать? (имя, телефон, комментарий): '

name_text = 'имя'
phone_text = 'телефон'
comment_text = 'комментарий'

new_name = 'Введите новое имя: '
new_phone = 'Введите новый номер: '
new_comment = 'Введите новый коммент: '




def add_successful(name: str) -> str:
    return f'Контакт {name} успешно добавлен!'


def delete_cnt(name, comment: str) -> str:
    return f'Контакт {name} {comment} успешно удален!'


def empty_search(word: str) -> str:
    return f'Контакты содержащие {word} не найдены!'


def change_field(word: str) -> str:
    return f'Поле {word} успешно изменено!'




