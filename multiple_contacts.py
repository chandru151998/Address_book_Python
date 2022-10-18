import logging


class Contact:

    def __init__(self, contacts_dict):
        self.first_name = contacts_dict.get("first_name")
        self.last_name = contacts_dict.get("last_name")
        self.address = contacts_dict.get("address")
        self.city = contacts_dict.get("city")
        self.state = contacts_dict.get("state")
        self.country = contacts_dict.get("country")
        self.pin = contacts_dict.get("pin")
        self.phone = contacts_dict.get("phone")
        self.email = contacts_dict.get("email")


class AddressBook:

    def __init__(self, address_book_name):
        self.address_book_name = address_book_name
        self.contact_dict = {}

    def add_contact(self, contact_object):
        """
        Function to add contact_object into dictionary
        :param contact_object: Contact object
        """
        self.contact_dict.update({contact_object.first_name: contact_object})

    def display_names(self):
        """
        Function to display contact names in address book
        """
        try:
            if self.contact_dict == {}:
                print("No contacts to display")
            else:
                for key, value in self.contact_dict.items():
                    print(key)
        except Exception as e:
            print(e)
            logging.exception(e)

    def get_contact_object(self, name):
        """
        Function to get contact object
        :param name: string
        :return: object of Contct
        """
        return self.contact_dict.get(name)

    def display_contacts(self):
        """
        Function to display contact details
        """
        try:
            if self.contact_dict == {}:
                print("No contacts to display")
            else:
                for key, value in self.contact_dict.items():
                    print("First Name : {}\nLast Name : {}\nAddress : {}\nCity : {}\nState : {}\nCountry : {}\n"
                          "PIN : {}\nPhone : {}\nEmail : {}"
                          .format(value.first_name, value.last_name, value.address, value.city, value.state,
                                  value.country, value.pin, value.phone, value.email))
        except Exception as e:
            print(e)
            logging.exception(e)

    def update_contact(self, contact_object, contacts_dictionary):
        """
        Function to update contact
        """
        try:
            contact_object.address = contacts_dictionary.get("update_address")
            contact_object.city = contacts_dictionary.get("update_city")
            contact_object.state = contacts_dictionary.get("update_state")
            contact_object.country = contacts_dictionary.get("update_country")
            contact_object.pin = contacts_dictionary.get("update_pin")
            contact_object.phone = contacts_dictionary.get("update_phone")
            contact_object.email = contacts_dictionary.get("update_email")

        except Exception as e:
            print(e)
            logging.exception(e)

    def delete_contact(self, name):
        """
        Function to remove contact
        :param name:
        """
        self.contact_dict.pop(name, "Contact name not present")


def add_contact():
    """
    Function to add a contact
    """
    try:
        first_name = input("Enter first name : ")
        last_name = input("Enter last name : ")
        address = input("Enter address : ")
        city = input("Enter city : ")
        state = input("Enter state : ")
        country = input("Enter country : ")
        pin = int(input("Enter zip code : "))
        phone = int(input("Enter phone number : "))
        email = input("Enter email id : ")

        contact_parameters = {"first_name": first_name, "last_name": last_name, "address": address, "city": city,
                              "state": state, "country": country, "pin": pin, "phone": phone, "email": email}
        contact = Contact(contact_parameters)

        address_book.add_contact(contact)

    except Exception as e:
        print(e)
        logging.exception(e)


def display_names():
    """
    Function to display contacts
    """
    address_book.display_names()


def display_contacts():
    """
    Function to display all contacts in address book
    """
    address_book.display_contacts()


def update_contact():
    """
    Function to update contact
    """
    name = input("Enter contact name to update : ")
    contact_object = address_book.get_contact_object(name)
    if not contact_object:
        print("Contact not present")
    else:
        update_address = input("Enter new address to update : ")
        update_city = input("Enter new city to update : ")
        update_state = input("Enter new state to update : ")
        update_country = input("Enter new country to update : ")
        update_pin = int(input("Enter new pin to update : "))
        update_phone = int(input("Enter new phone to update : "))
        update_email = input("Enter new email id to update : ")

        update_dict = {"update_address": update_address, "update_city": update_city, "update_state": update_state,
                       "update_country": update_country, "update_pin": update_pin, "update_phone": update_phone,
                       "update_email": update_email}

        address_book.update_contact(contact_object, update_dict)


def delete_contact():
    """
    Function to remove a contact
    """
    name = input("Enter first name to delete contact : ")
    address_book.delete_contact(name)


if __name__ == "__main__":
    try:
        address_book = AddressBook("Personal")

        while True:
            choice = int(input("1. Add new contact\n2. Show all names in address book\n3. Show contact info\n"
                               "4. Update contact\n5. Delete contact\n0. Exit\nEnter your choice : "))

            choice_dictionary = {1: add_contact, 2: display_names, 3: display_contacts, 4: update_contact,
                                 5: delete_contact}
            if choice == 0:
                break
            elif choice > 5:
                print("Please enter correct choice")
            else:
                choice_dictionary.get(choice)()

    except Exception as err:
        print(err)
        logging.exception(err)