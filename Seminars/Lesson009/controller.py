import text
import view
import modul

def start():
    pb = modul.Notes()
    while True:
        select = view.menu()
        match select:
            case 1:
                if pb.open_file():
                    view.print_message(text.load_successful)
                else:
                    view.print_message(text.error_load)
            case 2:
                if pb.save_file():
                    view.print_message(text.save_successful)
                else:
                    view.print_message(text.error_save)
            case 3:
                view.show_contacts(pb.get(), text.empty_book)
            case 4:
                new = view.add_contact()
                pb.add_contact(new)
                view.print_message(text.add_successful(new.get('name')))
            case 5:
                word = view.search_word()
                result = pb.search(word)
                view.show_contacts(result, text.empty_search(word))
            case 6:
                word = view.search_word()
                pb.change(word)
            case 7:
                word = view.search_word()
                pb.delete(word)
            case 8:
                if pb.chech_on_exit():
                    answer = view.change_confirm()
                    if answer.lower() == 'да':
                        pb.save_file()
                view.print_message(text.goodbay)
                break
