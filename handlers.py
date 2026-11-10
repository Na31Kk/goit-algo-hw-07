from models import AddressBook, Record

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Give me name and phone please."
    return inner

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)   
    if record is None:
        message = "Contact not found."
    else:
        record.edit_phone(old_phone, new_phone)
        message = "Contact updated."
    return message

@input_error
def get_contact(args, book: AddressBook):
    name = args[0]
    record = book.find(name)   
    if record is None:
        return "Contact not found."
    else:
        return record

@input_error
def get_all_contacts(book: AddressBook):
    if not book.data:
        return "No contacts found."
    else:
        return str(book)

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    else:
        record.add_birthday(birthday)
        return "Birthday added."

@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)   
    if record is None:
        return "Contact not found."
    elif record.birthday is None:
        return "No birthday set for this contact."
    else:
        return record.birthday.value

@input_error
def birthdays(book: AddressBook):
    upcoming_birthday = book.get_upcoming_birthday()
    if not upcoming_birthday:
        return "No upcoming birthdays in the next 7 days"
    results = []
    for item in upcoming_birthday:
        name = item.get("name")
        birthday = item.get("congratulation_date")
        results.append(f"{name}: {birthday}")
    return "\n".join(results)    