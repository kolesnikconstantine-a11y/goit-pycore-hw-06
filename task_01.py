from collections import UserDict


# Розробіть систему для керування адресною книгою.

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
    # реалізація класу
    # Реалізовано валідацію номера телефону (має бути перевірка на 10 цифр).
    def __init__(self, value):
        
             if len(value) > 1:
                  self.value = value
             else:
                  raise Exception("Phone must be 10 digits")

# Клас для зберігання інформації про контакт, включно з іменем та списком телефонів.
# Додавання телефонів.
# Видалення телефонів.
# Редагування телефонів.
# Пошук телефону.
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones: list[Phone] = []

    # реалізація класу
    # Реалізовано зберігання об'єкта Name в окремому атрибуті.
    # Реалізовано зберігання списку об'єктів Phone в окремому атрибуті.
    # Реалізовано методи для додавання — add_phone /
    #  видалення — remove_phone /
    #  редагування — edit_phone / 
    # пошуку об'єктів Phone — find_phone.

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def show_phone(self):
          print('+++ '.join(p.value for p in self.phones))
    

# Клас для зберігання записів та керування ними.
# Додавання записів.
    def add_phone(self, phone):
        self.phones.append(Phone(phone)) 

    # редагування — edit_phone
    def edit_phone(self, old_phone, new_phone):
          #print(self.name)
         #fr p, in self.phones:
            print(self.phones)
          #index = self.phones.index(old_phone)
         # self.phones[index] = new_phone
    
    # пошуку об'єктів Phone — find_phone.      
    def find_phone(self, phone):
          return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    # видалення — remove_phone
    def remove_phone(self, phone):
          self.phones.remove(Phone(phone)) 
    



# Функціональність: AddressBook
#1) Додавання записів. Реалізовано метод add_record, який додає запис до self.data.
#2) Пошук записів за іменем. Реалізовано метод find, який знаходить запис за ім'ям.
#3) Видалення записів за іменем. Реалізовано метод delete, який видаляє запис за ім'ям.

# AddressBook: Клас для зберігання записів та керування ними.
class AddressBook(UserDict):
    
    # Реалізовано метод add_record, який додає запис до self.data.
    # це значить до адресної книги
    def add_record(self, info: Record):
        self.data[info.name.value] = info
    
    # Реалізовано метод find, який знаходить запис за ім'ям.
    def find(self, name):
         return self.data.get(name)    
         
   
    # Реалізовано метод delete, який видаляє запис за ім'ям.
    def delete(self, name):
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
    #print(name)
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.show_phone()
john.edit_phone("1234567890", "1112223333")

#print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555
#print(jane)

    # Пошук конкретного телефону в записі John
#found_phone = john.find_phone("5555555555")
#print(john.name)
#print(john.phones)
#print(jane.name)
#print(jane.phones)
#print(f"{john.name}: {found_phone}")  # Виведення: 5555555555


# Видалення запису Jane
#book.delete("Jane")

# Виведення всіх записів у книзі
#for name, record in book.data.items():
#    #print(name)
#    print(record)
