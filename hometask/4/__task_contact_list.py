class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        contact_list = [self.name, self.phone]

    def __str__(self):
        return f'{self.name} - {phone}'


contacts = list()
choise = ''

while choise != '4':
    print('''1. Add contact 
2. Find contact 
3. Print all 
4. Exit''')

    choise = input('Select one of above: ')

    if choise == '1':
        name = input('Enter the name of the contact: ')
        phone = input('Enter the phone number: ')

        new_contact = Contact(name, phone)
        contacts.append(new_contact)
        print('New contact has been added')

    elif choise == '2':
        find_contact = input('Enter the search data: ')
        for i, contact in enumerate(contacts, 1):
            if find_contact in contact.__str__():
                print(f'{i}. {contact}')

    elif choise == '3':
        for i, contact in enumerate(contacts, 1):
            print(f'{i}. {contact}')
    elif choise == 4:
        break