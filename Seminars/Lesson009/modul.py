import json
import text
import view




class Notes:

    def __init__(self, path: str = 'Notes.json'):
        self.contact: dict = {}
        self.not_changed = {}
        self.path = path



    def get(self, index: int | None = None):
        if index:
            return self.contact.get(index)
        return self.contact

    def open_file(self):
        try:
            with open(self.path, 'r', encoding='UTF-8') as file:
                self.contact = json.load(file)
                self.not_changed = self.contact.copy()
            return True
        except:
            return False


    def save_file(self):
        try:
            with open(self.path, 'w', encoding='UTF-8') as file:
                json.dump(self.contact, file, ensure_ascii=False, indent=4)
            return True
        except:
            return False


    def check_id(self):
        if self.contact:
            return max(list(map(int, self.contact))) + 1
        return 1


    def add_contact(self, new: dict[str, str]):
        contact = {self.check_id(): new}
        self.contact.update(contact)


    def search(self, word: str) -> dict[int:dict[str, str]]:
        result = {}
        for index, contact in self.contact.items():
            if word.lower() in ' '.join(contact.values()).lower():
                result[index] = contact
        return result


    def delete(self, word: str) -> dict[int:dict[str, str]]:
        result = self.search(word)
        if result:
            view.show_contacts(result, text.empty_search(word))
            index = view.index_delete()
            delete_contact = self.contact.pop(index)
            view.print_message(text.delete_cnt(delete_contact.get('name'),
                                               delete_contact.get('comment')))
            return delete_contact


    def change(self, word: str) -> dict[int:dict[str, str]]:
        result = self.search(word)
        view.show_contacts(result, text.empty_search(word))
        if result:
            index = view.index_change()
            name_field = view.change_field()
            match name_field:
                case '1':
                    self.contact[index]['name'] = view.new_name()
                    view.print_message(text.change_field(text.name_text))
                case '2':
                    self.contact[index]['comment'] = view.new_comment()
                    view.print_message(text.change_field(text.comment_text))

                case _:
                    view.print_message(text.error_case_change)


    def chech_on_exit(self):
        if self.contact == self.not_changed:
            return False
        return True




