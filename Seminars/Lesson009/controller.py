import text
import view
import modul

def start():
    while True:
        select = view.menu()
        match select:
            case 1:
                if modul.open_file():
                   view.print_message(text.load_successful)
                else:
                    view.print_message(text.error_load)
            case 2:
                if modul.save_file():
                    view.print_message(text.save_successful)
                else:
                    view.print_message(text.error_save)
            case 3:
                view.show_contacts(modul.phone_book, text.empty_book)
            case 4:
                new = view.add_contact()
                modul.add_contact(new)
                view.print_message(text.add_successful(new.get('name')))
            case 5:
                word = view.search_word()
                result = modul.search(word)
                view.show_contacts(result, text.empty_search(word))
            case 6:
                word = view.search_word()
                modul.change(word)
            case 7:
                word = view.delete_word()
                delete_cnt = modul.delete(word)
                view.print_message(text.delete_cnt(delete_cnt.get('name'),
                                                   delete_cnt.get('comment')))

            case 8:
                break
