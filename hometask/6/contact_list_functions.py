import validators
import phonenumbers
import pandas

contacts = []

def add_contact():
    global name
    name = input("Enter the name of the contact: ")
    validators.valid_name()
    global phone
    phone = phonenumbers.parse(input("Enter the phone number: "), None)
    validators.valid_phone()
    global email
    email = input("Enter the e-mail of the contact: ")
    validators.valid_email()
    new_contact = (
        name,
        phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
        email,)
    contacts.append(new_contact)

    with open("contact.csv", "a") as f:
        for new_contact in contacts:
            f.writelines(f"{name} - {phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)} - {email} \n")
    print("New contact has been added")


def find_contact():
    find_contacts = input("Enter the search data: ")
    with open("contact.csv", "r") as f:
        for i, contact in enumerate(f, 1):
            if find_contacts in contact:
                print(f"{i}. {contact}")


def view_contacts():
    with open("contact.csv", "r") as f:
        for i, contact in enumerate(f, 1):
            print(f"{i}. {contact}")

def delete_contact():
    df = pandas.read_csv('contact.csv')
    print(df)
    remove = int(input("Which contact would you like to delete? "))
    df.drop([remove])
