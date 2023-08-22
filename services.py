# Классы для работы с телефонной книгой.
from typing import Dict, List


class Contact:
    """
    Класс контакта - записи в телефонном справочнике.
    Attrs:
    - index - индекс записи
    - last_name - Фамилия (кириллицей)
    - first_name - Имя (кириллицей)
    - patronymic - Отчество (кириллицей)
    - organization - Название организации (кириллицей)
    - work_phone - рабочий телефон в формате +7(9XX)XXX-XX-XX
    - mobile_phone - мобильный телефон в формате +7(9XX)XXX-XX-XX
    """
    def __init__(
            self, index: str, last_name: str, first_name: str,
            patronymic: str, organization: str,
            work_phone: str, mobile_phone: str):
        self.index = index
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.organization = organization
        self.work_phone = work_phone
        self.mobile_phone = mobile_phone

    def __repr__(self) -> str:
        return f"""{self.index}.
ФИО:{self.last_name} {self.first_name} {self.patronymic}
Организация: {self.organization}
Рабочий телефон: {self.work_phone}
Мобильный телефон: {self.mobile_phone}"""


class PhoneBook:
    """
    Класс телефонной книги.
    Attrs:
    - filename - файл, на основе которого создается
    и заполняется телефонная книга
    - contacts - список контактов из телефонной книги
    - last_index - индекс последнего добавленного контакта
    """

    def __init__(self, filename: str):
        self.filename = filename
        self.contacts = []
        self.upload_contacts()
        self.last_index = int(self.contacts[-1].index)

    def upload_contacts(self) -> None:
        """
        Функция загружает данные из файла (телефонного справочника)
        в список для быстрого доступа.
        """
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.split(';')
                new_contact = Contact(*data)
                self.contacts.append(new_contact)

    def paginate(self, data, page_size: int):
        """
        Генератор для постраничной пагинации записей справочника.
        """
        page = []
        for item in data:
            page.append(item)
            if len(page) >= page_size:
                yield page
                page = []
        if page:
            yield page

    def get_all_contacts(self) -> List[Contact]:
        """
        Функция для вывода постранично записей из справочника на экран.
        """
        return self.contacts

    def create_contact(
            self, last_name, first_name, patronymic,
            organization, work_phone, mobile_phone
    ) -> Contact:
        """
        Функция для добавления новой записи в справочник.
        """
        index = self.last_index + 1
        with open(self.filename, 'a') as file:
            file.write(f"""{index};{last_name};{first_name};\
{patronymic};{organization};{work_phone};{mobile_phone}\n""")
        new_contact = Contact(
            index, last_name, first_name,
            patronymic, organization, work_phone, mobile_phone)
        self.contacts.append(new_contact)
        self.last_index += 1
        return new_contact

    def update_contact(
            self, update_index: int, updated_contact: Contact) -> None:
        """
        Функция для добавления изменения существующей записи в справочнике.
        """
        self.contacts[update_index] = updated_contact
        self.save_contacts_to_csv()

    def save_contacts_to_csv(self) -> None:
        """
        Функция обновляет справочник.
        """
        try:
            with open(self.filename, 'w') as file:
                for contact in self.contacts:
                    file.write(
                        f"""{contact.index};{contact.last_name};{contact.first_name};\
{contact.patronymic};{contact.organization};\
{contact.work_phone};{contact.mobile_phone}""")
        except Exception as e:
            print(e)

    def get_contact(self, search_params: Dict[str, str]) -> List[Contact]:
        """
        Функция ищет запись с заданными характеристиками в списке контактов.
        """
        results = []
        for contact in self.contacts:
            search_res = all(
                            [getattr(contact, key) == value.capitalize()
                                for key, value in search_params.items()
                                if value])
            if search_res:
                results.append(contact)
        return results
