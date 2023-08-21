import readchar
from constants import PHONE_BOOK_FILE_NAME, PER_PAGE, ESC_KEY_CODE


class Contact:
    """
    Класс представляет информацию о записи в справочнике.
    фамилия, имя, отчество, название организации, телефон рабочий, телефон личный (сотовый)
    """
    def __init__(
            self, index, last_name, first_name,
            patronymic, organization,
            work_phone, mobile_phone):
        self.index = index
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.organization = organization
        self.work_phone = work_phone
        self.mobile_phone = mobile_phone

    def __repr__(self) -> str:
        return f"{self.index}. ФИО:{self.last_name} {self.first_name} {self.patronymic}. Организация: {self.organization}, Рабочий телефон: {self.work_phone}, Сотовый: {self.mobile_phone}"


class PhoneBook:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = []
        self.upload_contacts()
        self.last_index = int(self.contacts[-1].index)

    def upload_contacts(self):
        """
        Функция загружает данные из файла (телефонного справочника) в список для быстрого доступа.
        """
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.split(';')
                new_contact = Contact(*data)
                self.contacts.append(new_contact)

    def paginate(self, data, page_size):
        page = []
        for item in data:
            page.append(item)
            if len(page) >= page_size:
                yield page
                page = []
        if page:
            yield page

    def get_all_contacts(self):
        """
        Функция для вывода постранично записей из справочника на экран.
        """
        return self.contacts

    def create_contact(self, last_name, first_name, patronymic, organization, work_phone, mobile_phone):
        """
        Функция для добавления новой записи в справочник.
        """
        index = self.last_index + 1
        with open(self.filename, 'a') as file:
            file.write(f"{index};{last_name};{first_name};{patronymic};{organization};{work_phone};{mobile_phone}\n")
        new_contact = Contact(index, last_name, first_name, patronymic, organization, work_phone, mobile_phone)
        self.contacts.append(new_contact)
        self.last_index += 1
        return new_contact

    def update_contact(self, update_index, updated_contact):
        """
        Функция для добавления изменения существующей записи в справочнике.
        """
        self.contacts[update_index] = updated_contact
        self.save_contacts_to_csv()

    def save_contacts_to_csv(self):
        """
        Функция обновляет справочник.
        """
        try:
            with open(self.filename, 'w') as file:
                for contact in self.contacts:
                    file.write(f"{contact.index};{contact.last_name};{contact.first_name};{contact.patronymic};{contact.organization};{contact.work_phone};{contact.mobile_phone}")
        except Exception as e:
            print(e)

    def get_contact(self, **kwargs):
        """
        Функция ищет запись с заданными характеристиками в списке контактов.
        """
        results = []
        for contact in self.contacts:
            match = all(getattr(contact, attr) == value for attr, value in kwargs.items())
            if match:
                results.append(contact)
        return results