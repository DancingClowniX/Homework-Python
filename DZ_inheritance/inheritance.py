class Contact:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
    def display_info(self):
        print(f'Имя: {self.name}, Номер: {self.phone}')

class Company(Contact):
    def __init__(self,name,phone,company):
        super().__init__(name,phone)
        self.company = company
    def display_info(self):
        #super().display_info()
        print(f'Имя: {self.name}, Номер: {self.phone}, Компания: {self.company}')
class PhoneBook:
    def __init__(self):
        self.contacts = []
    def add_contact(self,contact):
        self.contacts.append(contact)
    def display_contacts(self):
        for contact in self.contacts:
            contact.display_info()
    def removeContact(self,name):
        for contact in self.contacts:
            if contact.name == name:
                print(f'{contact.name} удалён из книги')
                self.contacts.remove(contact)
    def findContact(self,name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None
phoneBook = PhoneBook()
contact1 = Contact("Victor Pyrra",'89021599360')
company_contact1 = Company("Jhon Doe",'89002020969','PizzaHot')
phoneBook.add_contact(contact1)
phoneBook.add_contact(company_contact1)
print("Список всех контактов: ")
phoneBook.display_contacts()
search_contact = input("введите имя контакта для поиска по тел книге: ")
found_contact = phoneBook.findContact(search_contact)
if found_contact:
    print("Найден контакт:")
    found_contact.display_info()
else:
    print("Контакт не найден")
search_contact1 = input("введите имя контакта для удаления: ")
Del_contact = phoneBook.removeContact(search_contact1)
phoneBook.display_contacts()