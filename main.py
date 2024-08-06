from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    # реалізація класу
		pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
          self.phones.append(phone)

    def remove_phone(self, phone_to_remove):
          for phone in self.phones:
                if phone == phone_to_remove:
                    index = self.phones.index(phone)
                    self.phones.pop(index)

    def edit_phone(self, old, new):
        for phone in self.phones:
            if phone != old:
                comment = 'we dont have such number, try another'
                raise ValueError(comment)
            else:
                self.remove_phone(old)
                self.add_phone(new)

    def __str__(self):
        phones_str = '; '.join(self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"
        

class AddressBook(UserDict):
    def add_record(self, record):
        pass


book = AddressBook()

john_record = Record("John")

john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")

print(john_record)
# print(jane_record)


print(john_record)
# print(jane_record)