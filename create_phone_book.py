# Дополнительный модуль для создания и заполнения
# телефонной книги тестовыми данными.
# В качестве фамилии, имени, отчества
# и названия организации берутся случайные слова из списка
# "Новый частотный словарь русской лексики" О. Н. Ляшевская, С. А. Шаров.

from random import randrange, sample
from typing import List

from constants import PHONE_BOOK_FILE_NAME, TEST_DATA_SIZE


def load_common_words() -> List[str]:
    """
    Функция читает файл и возвращает список самых частых русских слов.
    """
    with open('most_common_rus_words.txt') as common_words:
        return common_words.readlines()


def generate_random_phone() -> str:
    """
    Функция генерирует случайный номер телефона в формате +7(9XX)XXX-XX-XX.
    """
    number = "".join([str(i) for i in sample(range(10), 9)])
    return f"+7(9{number[0:2]}){number[2:5]}-{number[5:7]}-{number[7:9]}"


def generate_contact(common_words, index) -> str:
    """
    Функция генерирует случайные контактные данные
    для записи в телефонную книгу.
    """
    last_name = common_words[randrange(1000)].split('\n')[0].capitalize()
    first_name = common_words[randrange(1000)].split('\n')[0].capitalize()
    patronymic = common_words[randrange(1000)].split('\n')[0].capitalize()
    organization = common_words[randrange(1000)].split('\n')[0].capitalize()
    work_phone = generate_random_phone()
    mobile_phone = generate_random_phone()
    return f"""{index};{last_name};{first_name};\
{patronymic};ООО {organization};{work_phone};{mobile_phone}\n"""


def cvs_writer(data) -> None:
    """
    Функция записывает список с контактными данными в телефонную книгу.
    """
    with open(PHONE_BOOK_FILE_NAME, 'w') as file:
        for line in data:
            file.write(line)


def main():
    """
    Функция генерирует случайные данные и записывает в телефонную книгу.
    В константах можно задать произвольное количество строк для записи,
    по умолчанию 1000.
    """
    common_words = load_common_words()
    new_contacts = [
        generate_contact(common_words, i+1) for i in range(TEST_DATA_SIZE)]
    cvs_writer(new_contacts)


if __name__ == "__main__":
    main()
