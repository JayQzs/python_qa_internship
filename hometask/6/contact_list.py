import contact_list_functions
import sys

def main():
    while True:
        choise = int(
            input(
                "1. Add contact\n"
                "2. Find contact\n"
                "3. View all contacts\n"
                "4. Delete contact\n"
                "5. Exit\n"
                "Select one of above: "
            )
        )
        if choise == 1:
            contact_list_functions.add_contact()
        if choise == 2:
            contact_list_functions.find_contact()
        if choise == 3:
            contact_list_functions.view_contacts()
        if choise == 4:
            contact_list_functions.delete_contact()
        if choise == 5:
            sys.exit("You exit the contact list")


main()


