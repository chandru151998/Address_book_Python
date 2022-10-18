import csv
import json
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

    def get_contact_dict(self):
        """
        Function to create a dictionary containing attribute values of contact
        :return: Contact attribute value
        """
        return {"first_name": self.first_name, "last_name": self.last_name, "address": self.address, "city": self.city,
                "state": self.state, "country": self.country, "pin": self.pin, "phone": self.phone, "email": self.email}

    def as_string(self):
        return "{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}"\
            .format(self.first_name, self.last_name, self.address, self.city, self.state, self.country, self.pin,
                    self.phone, self.email)



class AddressBook:

    def __init__(self, address_book_name):
        self.address_book_name = address_book_name
        self.contact_dict = {}

    def add_contact(self, contact_object):
        """
        Function to add contact_object into dictionary
        :param contact_object: object containing contact attribute values
        :return: none
        """
        self.contact_dict.update({contact_object.first_name: contact_object})

    def display_contact_names(self):
        """
        Function to display contact names in address book
        :return: none
        """
        try:
            if len(self.contact_dict) == 0:
                print("No contacts to display")
            else:
                for key, value in self.contact_dict.items():
                    print("{:<10} {:<10}".format('Contact name', key))

        except Exception as e:
            logging.exception(e)

    def get_contact_object(self, name):
        """
        Function to get contact object
        :param name: string name from dictionary
        :return: string name from contact_dict dictionary
        """
        return self.contact_dict.get(name)

    def display_contacts(self):
        """
        Function to display contact details
        :return: none
        """
        try:
            if len(self.contact_dict) == 0:
                print("No contacts to display")
            else:
                print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format
                      ('First Name', 'Last Name', 'Address', 'City', 'State', 'Country', 'PIN', 'Phone', 'Email'))
                for key, value in self.contact_dict.items():
                    print(value.as_string())

        except Exception as e:
            logging.exception(e)

    def update_contact(self, contact_object, contacts_dictionary):
        """
        Function to update contact
        :param contact_object: contains name from addressbook
        :param contacts_dictionary: dictionary containing contact attribute values
        :return: none
        """
        try:
            contact_object.first_name = contacts_dictionary.get("update_first_name")
            contact_object.last_name = contacts_dictionary.get("update_last_name")
            contact_object.address = contacts_dictionary.get("update_address")
            contact_object.city = contacts_dictionary.get("update_city")
            contact_object.state = contacts_dictionary.get("update_state")
            contact_object.country = contacts_dictionary.get("update_country")
            contact_object.pin = contacts_dictionary.get("update_pin")
            contact_object.phone = contacts_dictionary.get("update_phone")
            contact_object.email = contacts_dictionary.get("update_email")

        except Exception as e:
            logging.exception(e)

    def delete_contact(self, name):
        """
        Function to remove contact
        :param name: string name from contact_dict dictionary
        :return: none
        """
        self.contact_dict.pop(name, f'{name} - Contact does not exist')

    def get_contacts_as_dict(self):
        """
        Function to return contact as a dictionary
        :return: contact_details dictionary
        """
        contact_details_dict = {}
        for key, value in self.contact_dict.items():
            contact_details_dict.update({value.first_name: value.get_contact_dict()})

        return contact_details_dict


class MultipleAddressBooks:

    def __init__(self):
        self.json_dict = {}
        self.address_book_dict = {}

    def add_address_book(self, address_book_object):
        """
        Function to add address_book_object to address_book_dict dictionary
        :param address_book_object:
        :return: none
        """
        self.address_book_dict.update({address_book_object.address_book_name: address_book_object})

    def get_address_book_object(self, name):
        """
        Function to get address_book_object
        """
        return self.address_book_dict.get(name)

    def display_address_book_names(self):
        """
        Function to show address book names
        """
        for key, value in self.address_book_dict.items():
            print("Address book name : ", key)

    def delete_address_book(self, name):
        """
        Function to delete address_book
        """
        self.address_book_dict.pop(name, f'{name} - Address Book does not present')

    def write_to_json_file(self):
        """
        Function to write address book contacts to a JSON file
        """
        # json_dictionary = {}
        for address_book_name, address_book_object in self.address_book_dict.items():
            contact_dictionary = address_book_object.get_contacts_as_dict()

            self.json_dict.update({address_book_name: contact_dictionary})

            json_object = json.dumps(self.json_dict, indent=4)
            with open("contact_info.json", "w") as write_file:
                write_file.write(json_object)

    def write_to_csv_file(self):
        """
        Function to write address book contacts to a CSV file
        """
        with open("contact_info.csv", "w", newline='') as write_file:
            fieldnames = ['first_name', 'last_name', 'address', 'city', 'state', 'country', 'pin', 'phone', 'email']

            csv_writer = csv.DictWriter(write_file, fieldnames=fieldnames)
            csv_writer.writeheader()

            for address_book_name, address_book_object in self.address_book_dict.items():
                contact_dictionary = address_book_object.get_contacts_as_dict()
                for key, value in contact_dictionary.items():
                    csv_writer.writerow(value)


def add_contact():
    """
    Function to add a contact
    """
    try:
        address_book_name = input("Enter Address Book name : ")
        address_book_object = multiple_address_book.get_address_book_object(address_book_name)
        if not address_book_object:
            address_book_object = AddressBook(address_book_name)
            multiple_address_book.add_address_book(address_book_object)
        first_name = input("Enter first name : ")
        if first_name == "":
            print("Please enter first name")
            return
        last_name = input("Enter last name : ")
        if last_name == "":
            print("Please enter last name")
            return
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

        address_book_object.add_contact(contact)
        multiple_address_book.write_to_json_file()
        multiple_address_book.write_to_csv_file()

    except Exception as e:
        logging.exception(e)


def display_names():
    """
    Function to display contacts
    """
    address_book_name = input("Enter Address Book name : ")
    address_book_object = multiple_address_book.get_address_book_object(address_book_name)
    address_book_object.display_contact_names()


def display_contacts():
    """
    Function to display all contacts in address book
    """
    address_book_name = input("Enter Address Book name : ")
    address_book_object = multiple_address_book.get_address_book_object(address_book_name)
    address_book_object.display_contacts()


def update_contact():
    """
    Function to update contact
    """
    try:
        address_book_name = input("Enter Address Book name : ")
        address_book_object = multiple_address_book.get_address_book_object(address_book_name)
        if not address_book_object:
            print(f'{address_book_object} address book does not exist')
            return
        name = input("Enter contact name to update : ")
        contact_object = address_book_object.get_contact_object(name)
        if not contact_object:
            print(f'{name} contact does not exist')
        else:
            last_name = input("Enter new last name to update : ")
            update_address = input("Enter new address to update : ")
            update_city = input("Enter new city to update : ")
            update_state = input("Enter new state to update : ")
            update_country = input("Enter new country to update : ")
            update_pin = int(input("Enter new pin to update : "))
            update_phone = int(input("Enter new phone to update : "))
            update_email = input("Enter new email id to update : ")

            update_dict = {"update_first_name": name, "update_last_name": last_name,
                           "update_address": update_address,
                           "update_city": update_city, "update_state": update_state, "update_country": update_country,
                           "update_pin": update_pin, "update_phone": update_phone, "update_email": update_email}

            address_book_object.update_contact(contact_object, update_dict)
            multiple_address_book.write_to_json_file()
            multiple_address_book.write_to_csv_file()

    except Exception as e:
        logging.exception(e)


def delete_contact():
    """
    Function to remove a contact
    """
    address_book_name = input("Enter Address Book name : ")
    address_book_object = multiple_address_book.get_address_book_object(address_book_name)
    name = input("Enter first name to delete contact : ")
    address_book_object.delete_contact(name)
    multiple_address_book.json_dict.clear()
    multiple_address_book.write_to_json_file()
    multiple_address_book.write_to_csv_file()


def display_address_book_names():
    """
    Function to display address book names
    """
    multiple_address_book.display_address_book_names()


def delete_address_book():
    """
    Function to delete address book
    """
    address_book_name = input("Enter Address Book name : ")
    multiple_address_book.delete_address_book(address_book_name)
    multiple_address_book.json_dict.clear()
    multiple_address_book.write_to_json_file()
    multiple_address_book.write_to_csv_file()


def read_from_json_file():
    """
    Function to read contacts from json file
    """
    with open("contact_info.json", "r") as read_file:
        json_object = json.load(read_file)
    for key, value in json_object.items():
        print("{:<10} {:<10}".format('Address Book Name', key))
        for i, j in value.items():
            for k, l in j.items():
                print("{:<10} {:<10}".format(k, l))
            print("-----------------")


def read_from_csv_file():
    """
    Function to read contacts from a CSV file
    """
    with open("contact_info.csv", "r") as read_file:
        csv_reader = csv.DictReader(read_file)

        for line in csv_reader:
            for key, value in line.items():
                print("{:<10} {:<10}".format(key, value))
            print("-----------------")


if __name__ == "__main__":
    multiple_address_book = MultipleAddressBooks()

    try:
        while True:
            choice = int(input("1.Add new contact\n2.Display address book names\n3.Display contact names\n"
                               "4.Display contact information\n5.Update contact\n6.Delete contact\n"
                               "7.Delete an Address Book\n8.Read JSON file\n"
                               "9.Read CSV file\n0.Exit\nEnter your choice : "))

            choice_dictionary = {1: add_contact, 2: display_address_book_names, 3: display_names, 4: display_contacts,
                                 5: update_contact, 6: delete_contact, 7: delete_address_book, 8: read_from_json_file,
                                 9: read_from_csv_file}
            if choice == 0:
                break
            elif choice > 9:
                print("Please enter correct choice")
            else:
                choice_dictionary.get(choice)()

    except Exception as e:
        logging.exception(e)
