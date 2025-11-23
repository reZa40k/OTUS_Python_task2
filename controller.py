from model import PhoneBookModel
from model import ContactNotFound
from view import PhoneBookView
import text

class PhoneBookController:
    def __init__(self):
        self.model = PhoneBookModel()
        self.view = PhoneBookView()

    def start_menu(self):
        '''
        Работа главного меню
        '''
        while True:
            self.view.show_menu()
            choice = self.view.input_user()

            if choice == 1:
                # Показать все контакты
                self.view.show_contacts(self.model.contacts, text.empty_phone_book_error)

            elif choice == 2:
                # Добавить контакт
                name, phone, comment = self.view.add_contact_view()
                new_id = self.model.add_contact(name, phone, comment)
                self.view.show_contacts(self.model.contacts, text.empty_phone_book_error)
                self.view.show_contacts(self.model.contacts, text.empty_phone_book_error)
                self.view.print_message(f"Контакт '{name}' добавлен с ID {new_id}")

            elif choice == 3:
                # Удалить контакт
                self.view.show_contacts(self.model.contacts, text.empty_phone_book_error)
                contact_id = self.view.delete_contact_view()
                if contact_id and self.model.delete_contact(contact_id):
                    self.view.print_message(f"Контакт с ID {contact_id} удалён")
                else:
                    self.view.print_message(f"Контакт с ID {contact_id} не найден")

            elif choice == 4:
                # Редактировать контакт
                self.view.show_contacts(self.model.contacts, text.empty_phone_book_error)
                contact_id, name, phone, comment = self.view.edit_contact_view()
                if contact_id and self.model.edit_contact(contact_id, name, phone, comment):
                    self.view.print_message(f"Контакт с ID {contact_id} обновлён")
                else:
                    self.view.print_message(f"Контакт с ID {contact_id} не найден")
                    
            elif choice == 5:
                search_name = self.view.search_contact_view()
                try:
                    results = self.model.search_contacts(search_name)
                    self.view.show_contacts(results, "Результаты поиска:")
                except ContactNotFound as e:
                    self.view.print_message(str(e))

            elif choice == 0:
                self.view.print_message(text.exit)
                break

            else:
                self.view.print_message("Некорректный выбор")
