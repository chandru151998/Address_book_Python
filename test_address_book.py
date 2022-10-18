import pytest
from address_book_pytest import Contact, AddressBook, MultipleAddressBooks


@pytest.fixture
def contact_object():
    return Contact({"first_name": "Chandru", "last_name": "K", "address": "Colony", "city": "Gsg", "state": "KA",
                    "country": "IND", "pin": 12345, "phone": 7406140157, "email": "amk@gmail.com"})


@pytest.fixture
def address_book_object():
    return AddressBook("My")


def test_add_contact(contact_object, address_book_object):
    assert len(address_book_object.contact_dict) == 0
    address_book_object.add_contact(contact_object)
    assert len(address_book_object.contact_dict) == 1


def test_for_contact(contact_object, address_book_object):
    address_book_object.add_contact(contact_object)
    assert contact_object == address_book_object.get_contact_object("Chandru")


def test_delete_contact_method(contact_object, address_book_object):
    address_book_object.add_contact(contact_object)
    address_book_object.delete_contact("Chandru")
    assert not address_book_object.get_contact_object(contact_object)


def test_add_address_book(address_book_object):
    multiple_address_book_object = MultipleAddressBooks()
    assert len(multiple_address_book_object.address_book_dict) == 0
    multiple_address_book_object.add_address_book(address_book_object)
    assert len(multiple_address_book_object.address_book_dict) == 1


def test_address_book(address_book_object):
    multiple_address_book_object = MultipleAddressBooks()
    multiple_address_book_object.add_address_book(address_book_object)
    assert address_book_object == multiple_address_book_object.get_address_book_object("My")


def test_delete_address_book(address_book_object):
    multiple_address_book_object = MultipleAddressBooks()
    multiple_address_book_object.add_address_book(address_book_object)
    multiple_address_book_object.delete_address_book("My")
    assert not multiple_address_book_object.get_address_book_object("My")

