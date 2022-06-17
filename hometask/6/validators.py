import phonenumbers
from pyisemail import is_email
import contact_list_functions

def valid_name():
    if len(contact_list_functions.name) <= 3:
        print("The length of the name can't be less than 3 symbols!")
        name = input("Enter the name of the contact: ")
    else:
        print("Correct, continue entering the contact's data.")

def valid_phone():
    if not phonenumbers.is_valid_number(contact_list_functions.phone) == True:
        print("This number is not correct. Please, enter the valid phone number")
        phone = phonenumbers.parse(input("Enter the phone number: "))
    else:
        print("Correct, continue entering the contact's data.")

def valid_email():
    if is_email(contact_list_functions.email, allow_gtld=False, check_dns=False) == False:
        print("Fail: ", is_email(contact_list_functions.email, diagnose=True))
        email = input("Please, enter the valid e-mail: ")
    else:
        print("Success")