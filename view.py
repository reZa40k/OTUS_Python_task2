
class PhoneBookView:

    def show_menu(self):
        '''
        Открываем меню телефонного справочника
        '''
        # while True:
        print("\n\tТелефонный справочник")
        print("1. Показать все контакты")
        print("2. Добавить контакт")
        print("3. Удалить контакт")
        print("4. Редактировать контакт")
        print("5. Поиск контактов")
        print("0. Выйти")
            
    def input_user(self):
        '''
        Запрашиваем ввод необходимого действия в меню
        '''
        while True:
            try:
                number = int(input("Выберите действие: "))
                if number in [0, 1, 2, 3, 4, 5]:
                    return number
                else:
                    print("\nОшибка. Выберите корректный номер меню")
            except ValueError:
                print("\nВведите целое число из списка")        
        
    def show_contacts(self,contacts, message_error):
        '''
        Выводим список всех контактов
        '''
        print("\nСписок контактов:")
        if contacts:
            for idx, contact in contacts.items():
                print(f"{idx:>3}. {contact.name:<25} {contact.phone:<25} {contact.comment:<25}")
        else:
            print(message_error)
            
            
    def add_contact_view(self):
        '''
        Добавляем новый контакт
        '''
        print("\nДобавление нового контакта:")
        name = input("Имя: ")
        phone = input("Телефон: ")
        comment = input("Описание: ")
        return name, phone, comment

    def delete_contact_view(self):
        '''
        Удаляем контакт по ID
        '''
        try:
            contact_id = int(input("Введите ID контакта для удаления: "))
            return contact_id
        except ValueError:
            print("\nВведите ID из списка")
            return None

    def edit_contact_view(self):
        '''
        Редактируем контакт по ID
        '''
        try:
            contact_id = int(input("Введите ID контакта для редактирования: "))
            name = input("Новое имя: ")
            phone = input("Новый телефон: ")
            comment = input("Новое описание: ")
            return contact_id, name, phone, comment
        except ValueError:
            print("\nВведите ID из списка")
            return None, None, None, None
        
    def search_contact_view(self):
        name = input("Введите ключевое слово для поиска: ")
        return name

    def print_message(self, message):
        print(message)