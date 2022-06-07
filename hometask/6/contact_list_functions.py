import phonenumbers
from pyisemail import is_email
from tabulate import tabulate


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.phone}, {self.email}"


contacts = []


def add_contact():
    name = input("Enter the name of the contact: ")
    if len(name) <= 3:
        print("The length of the name can't be less than 3 symbols!")
        name = input("Enter the name of the contact: ")
    else:
        print("Correct, continue entering the contact's data.")
    phone = phonenumbers.parse(input("Enter the phone number: "), None)
    if not phonenumbers.is_valid_number(phone) == True:
        print("This number is not correct. Please, enter the valid phone number")
        phone = phonenumbers.parse(input("Enter the phone number: "))
    else:
        print("Correct, continue entering the contact's data.")
    email = input("Enter the e-mail of the contact: ")
    if is_email(email, allow_gtld=False, check_dns=False) == False:
        print("Fail: ", is_email(email, diagnose=True))
        email = input("Please, enter the valid e-mail: ")
    else:
        print("Success")
    new_contact = (
        name,
        phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
        email,
    )
    contacts.append(new_contact)
    print("New contact has been added")


def find_contact():
    find_contacts = input("Enter the search data: ")
    for i, contact in enumerate(contacts, 1):
        if find_contacts in contact.__str__():
            print(f"{i}. {contact}")


def view_contacts():
    print(tabulate(contacts))


def delete_contact():
    view_contacts()
    remove = int(input("Which contact would you like to delete? "))
    if 0 < remove < len(contacts):
        del contacts[remove - 1]
        print("The contact is deleted")
    else:
        print("Error, the contact isn't found!")
