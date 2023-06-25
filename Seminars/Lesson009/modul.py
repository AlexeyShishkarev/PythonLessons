import json
import text
import view

phone_book = {}

path = 'phones.json'


def open_file():
    global phone_book
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            phone_book = json.load(file)
        return True
    except:
        return False


def save_file():
    try:
        with open(path, 'w', encoding='UTF-8') as file:
            json.dump(phone_book, file, ensure_ascii=False)
        return True
    except:
        return False


def check_id():
    if phone_book:
        return max(list(map(int, phone_book))) + 1
    return 1


def add_contact(new: {int: dict[str, str]}):
    contact = {check_id(): new}
    phone_book.update(contact)


def search(word: str) -> dict[int:dict[str, str]]:
    result = {}
    for index, contact in phone_book.items():
        if word.lower() in ' '.join(contact.values()).lower():
            result[index] = contact
    return result


def delete(word: str) -> dict[int:dict[str, str]]:
    result = search(word)
    if result:
        view.show_contacts(result, text.empty_search(word))
        index = view.index_delete()
        delete_contact = phone_book.pop(index)
        view.print_message(text.delete_cnt(delete_contact.get('name'),
                                           delete_contact.get('comment')))
        return delete_contact






def change(word: str) -> dict[int:dict[str, str]]:
    result = search(word)
    view.show_contacts(result, text.empty_search(word))
    if result:
        index = view.index_change()
        name_field = view.change_field()
        match name_field:
            case text.name_text:
                phone_book[index]['name'] = view.new_name()
                view.print_message(text.change_field(text.name_text))
            case text.phone_text:
                phone_book[index]['phone'] = view.new_phone()
                view.print_message(text.change_field(text.phone_text))
            case text.comment_text:
                phone_book[index]['comment'] = view.new_comment()
                view.print_message(text.change_field(text.comment_text))





