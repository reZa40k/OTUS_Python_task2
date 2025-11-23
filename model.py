import json


PATH = "phone_book.json"

class Contact:
    def __init__(self, name, phone, comment):
        self.name = name
        self.phone = phone
        self.comment = comment
        
    @staticmethod
    def from_dict(data):
        '''
        Создаем контакт из словаря
        '''
        return Contact(data['name'], data['phone'], data['comment'])

    def to_dict(self):
        return {"name": self.name, "phone": self.phone, "comment": self.comment}
    
class ContactNotFound(Exception):
    pass
        
class PhoneBookModel:
    def __init__(self):
        self.contacts = {}
        self.load_phonebook()
        
    def load_phonebook(self):
        '''
        Загружаем справочник из json
        '''
        try:
            with open(PATH, 'r', encoding='UTF-8') as file:
                content = json.load(file)
    
            # Нумерация ключей
            self.contacts = {idx + 1: Contact.from_dict(contact) for idx, contact in enumerate(content)}
        except (FileNotFoundError, json.JSONDecodeError):
            self.contacts = {}  
            
    
    def save_phonebook(self):
        '''
        Сохраняем базу контактов
        '''
        data_list = [contact.to_dict() for contact in  self.contacts.values()]
        with open(PATH, 'w', encoding='UTF-8') as file:
            json.dump(data_list, file, indent=4, ensure_ascii=False)
    
    
    def add_contact(self, name, phone, comment):
        '''
        Добавляем новый контакт, сохраняем изменения
        '''
        new_id = max(self.contacts.keys(), default=0) + 1
        self.contacts[new_id] = Contact(name, phone, comment)
        self.save_phonebook()
        return new_id

    def delete_contact(self, contact_id):
        '''
        Удаляем контакт по ID, сохраняем изменения
        '''
        if contact_id in self.contacts:
            del self.contacts[contact_id]
            self.save_phonebook()
            return True
        return False

    def edit_contact(self, contact_id, name, phone, comment):
        '''
        Изменяем контакт по ID, сохраняем изменения
        '''
        if contact_id in self.contacts:
            self.contacts[contact_id].name = name
            self.contacts[contact_id].phone = phone
            self.contacts[contact_id].comment = comment
            self.save_phonebook()
            return True
        return False
    
    def search_contacts(self, keyword):
        '''
        Поиск контактов по ключевому слову
        '''
        try:
            keyword_lower = keyword.lower()
            results = {}
            for contact_id, contact in self.contacts.items():
                if (keyword_lower in contact.name.lower() or
                    keyword_lower in contact.phone.lower() or
                    keyword_lower in contact.comment.lower()):
                    results[contact_id] = contact
            if not results:
                raise ContactNotFound(f"Поиск по '{keyword}' ничего не нашел")
            return results
        except Exception as e:
            raise
        
    

    