import readchar
from constants import (
    PHONE_BOOK_FILE_NAME, ORGANIZATION_INPUT, WORK_PHONE_INPUT, 
    PER_PAGE, LAST_NAME_INPUT, FIRST_NAME_INPUT, MOBILE_INPUT, CHOICE_INPUT, 
    ESC_KEY_CODE, ENTER_KEY_CODE, PATRONYMIC_INPUT, CONTACT_CREATED, 
    MAIN_MENU, NEXT_OR_EXIT_TO_MENU)
from services import PhoneBook
from validators import (
    validate_name_cyrillic,
    validate_organization,
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
    last_name = first_name = patronymic = organization = work_phone = mobile_phone = None
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
    new_contact = phone_book.create_contact(last_name, first_name, patronymic, organization, work_phone, mobile_phone)
    print(CONTACT_CREATED.format(new_contact))


def update_contact(phone_book):
    update_index = int(input("Введите индекс записи, которую хотите изменить: ")) -1
    if 0 <= update_index < phone_book.last_index:
        updated_contact = phone_book.contacts[update_index]
        print("Введите поля, которые хотите изменить. Есл нет нажмите Enter для пропуска.")
        updated_contact.last_name = input(f"Фамилия кириллицей: ({updated_contact.last_name}): ") or updated_contact.last_name
        updated_contact.first_name = input(f"Имя кириллицей: ({updated_contact.first_name}): ") or updated_contact.first_name
        updated_contact.patronymic = input(f"Отчество кириллицей: ({updated_contact.patronymic}): ") or updated_contact.patronymic
        updated_contact.organization = input(f"Название организации: ({updated_contact.organization}): ") or updated_contact.organization
        updated_contact.work_phone = input(f"Рабочий телефон в формате +7(9XX)XXX-XX-XX: ({updated_contact.work_phone}): ") or updated_contact.work_phone
        updated_contact.mobile_phone = input(f"Мобильный телефон в формате +7(9XX)XXX-XX-XX: ({updated_contact.mobile_phone}): ") or updated_contact.mobile_phone
        phone_book.update_contact(update_index, updated_contact)
    else:
        print("Неверный индекс.")


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
            search_params = {}
            search_params['last_name'] = input("Фамилия: ")
            search_params['first_name'] = input("Имя: ")
            search_params['patronymic'] = input("Отчество: ")
            search_params['organization'] = input("Название организации: ")
            search_params['work_phone'] = input("Рабочий телефон: ")
            search_params['mobile_phone'] = input("Мобильный телефон: ")
            search_results = phone_book.get_contact(**search_params)
            if search_results:
                print("Результаты поиска:")
                for contact in search_results:
                    print(contact)

            else:
                print("Ничего не найдено.")
        elif choice == "5":
            break
        else:
            print("Пожалуйста, выберите пункт от 1 до 5.")



if __name__ == "__main__":
    main()
