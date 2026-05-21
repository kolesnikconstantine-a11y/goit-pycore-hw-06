from collections import UserDict

# Базовий клас для полів запису.
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# Клас для зберігання імені контакту. Обов'язкове поле.
class Name(Field):
    # реалізація класу
		pass

# Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
class Phone(Field):
    # Реалізовано валідацію номера телефону (має бути перевірка на 10 цифр).
    def __init__(self, value):
             if len(value) == 10:
                  self.value = value
             else:
                  raise Exception("Phone must be 10 digits only")

# Клас для зберігання інформації про контакт, включно з іменем та списком телефонів.
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones: list[Phone] = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
# Додавання записів add_phone
    def add_phone(self, phone):
        self.phones.append(Phone(phone)) 

    # редагування — edit_phone
    def edit_phone(self, old_phone, new_phone):
         for p in self.phones:
            if p.value == old_phone:
                 # ??? can't find index ???
                 #index = self.phones.index(p.value)
                 index = 0
                 self.phones[index] = Phone(new_phone)
    
    # пошуку об'єктів Phone — find_phone.      
    def find_phone(self, phone):
          for p in self.phones:
               if p.value == phone:
                    return p.value
    
    # видалення — remove_phone
    def remove_phone(self, phone):
          self.phones.remove(Phone(phone)) 
    
# AddressBook: Клас для зберігання записів та керування ними.
class AddressBook(UserDict):
    
    # Реалізовано метод add_record, який додає запис до self.data.
    def add_record(self, info: Record):
        self.data[info.name.value] = info
    
    # Реалізовано метод find, який знаходить запис за ім'ям.
    def find(self, name):
         return self.data.get(name)    
         
    # Реалізовано метод delete, який видаляє запис за ім'ям.
    def delete(self, name):
          if self.data[name]:
            del self.data[name]
          
# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону в записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")
