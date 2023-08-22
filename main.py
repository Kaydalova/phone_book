from typing import List

import readchar
from constants import (CHOICE_INPUT, CHOOSE_1_TO_5, CONTACT_CREATED,
                       CONTACT_UPDATED, ENTER_KEY_CODE, ENTER_OR_ESC,
                       ESC_KEY_CODE, FIRST_NAME_INPUT, INDEX_INPUT,
                       INVALID_INDEX, LAST_NAME_INPUT, MAIN_MENU, MOBILE_INPUT,
                       NEXT_OR_EXIT_TO_MENU, NOT_FOUND, ORGANIZATION_INPUT,
                       PATRONYMIC_INPUT, PER_PAGE, PHONE_BOOK_FILE_NAME,
                       SEARCH_INDEX, SEARCH_RESULTS, WORK_PHONE_INPUT)
from services import Contact, PhoneBook
from validators import (validate_name_cyrillic, validate_organization,
                        validate_phone)


def show_contacts(phone_book):
    contacts = phone_book.get_all_contacts()
    paginated_contacts = phone_book.paginate(contacts, PER_PAGE)
    for page in paginated_contacts:
        for contact in page:
            print(contact)
        print(NEXT_OR_EXIT_TO_MENU)
        key_bytes = readchar.readkey().encode()
        if key_bytes == ENTER_KEY_CODE:
            continue
        elif key_bytes == ESC_KEY_CODE:
            break
    return


def create_contact(phone_book):
    last_name = first_name = patronymic = '1'
    organization = '*'
    work_phone = mobile_phone = '1'
    while not validate_name_cyrillic(last_name):
        last_name = input(LAST_NAME_INPUT)
    while not validate_name_cyrillic(first_name):
        first_name = input(FIRST_NAME_INPUT)
    while not validate_name_cyrillic(patronymic):
        patronymic = input(PATRONYMIC_INPUT)
    while not validate_organization(organization):
        organization = input(ORGANIZATION_INPUT)
    while not validate_phone(work_phone):
        work_phone = input(WORK_PHONE_INPUT)
    while not validate_phone(mobile_phone):
        mobile_phone = input(MOBILE_INPUT)
    new_contact = phone_book.create_contact(
        last_name, first_name, patronymic,
        organization, work_phone, mobile_phone)
    print(CONTACT_CREATED.format(new_contact))


def update_contact(phone_book):
    update_index = int(input(SEARCH_INDEX)) - 1
    if 0 <= update_index < phone_book.last_index:
        updated_contact = phone_book.contacts[update_index]
        print(ENTER_OR_ESC)
        updated_contact.last_name = input(
            LAST_NAME_INPUT).capitalize() or updated_contact.last_name
        updated_contact.first_name = input(
            FIRST_NAME_INPUT).capitalize() or updated_contact.first_name
        updated_contact.patronymic = input(
            PATRONYMIC_INPUT).capitalize() or updated_contact.patronymic
        updated_contact.organization = input(
            ORGANIZATION_INPUT).capitalize() or updated_contact.organization
        updated_contact.work_phone = input(
            WORK_PHONE_INPUT) or updated_contact.work_phone
        updated_contact.mobile_phone = input(
            MOBILE_INPUT) or updated_contact.mobile_phone
        phone_book.update_contact(update_index, updated_contact)
        print(CONTACT_UPDATED.format(updated_contact))
    else:
        print(INVALID_INDEX)


def find_contact(phone_book) -> List[Contact]:
    search_params = {}
    search_params['index'] = input(INDEX_INPUT)
    search_params['last_name'] = input(LAST_NAME_INPUT)
    search_params['first_name'] = input(FIRST_NAME_INPUT)
    search_params['patronymic'] = input(PATRONYMIC_INPUT)
    search_params['organization'] = input(ORGANIZATION_INPUT)
    search_params['work_phone'] = input(WORK_PHONE_INPUT)
    search_params['mobile_phone'] = input(MOBILE_INPUT)
    search_results = phone_book.get_contact(search_params)
    return search_results


def main():
    phone_book = PhoneBook(PHONE_BOOK_FILE_NAME)

    while True:
        print(MAIN_MENU)
        choice = input(CHOICE_INPUT)
        if choice == "1":
            show_contacts(phone_book)
        elif choice == "2":
            create_contact(phone_book)
        elif choice == "3":
            update_contact(phone_book)
        elif choice == '4':
            search_results = find_contact(phone_book)
            if search_results:
                print(SEARCH_RESULTS)
                for contact in search_results:
                    print(contact)
            else:
                print(NOT_FOUND)
        elif choice == "5":
            break
        else:
            print(CHOOSE_1_TO_5)


if __name__ == "__main__":
    main()
