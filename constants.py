PHONE_BOOK_FILE_NAME = 'phone_book.csv'
PER_PAGE = 10
TEST_DATA_SIZE = 10_000
ESC_KEY_CODE = b'\x1b\x1b'
ENTER_KEY_CODE = b'\r'


# Тектсы для интерфейса
MAIN_MENU = """Телефонный справочник:
1. Показать записи постранично
2. Добавить запись
3. Редактировать запись
4. Поиск записей
5. Выход"""

NEXT_OR_EXIT_TO_MENU = """Нажмите Enter чтобы перейти на следующую страницу\
или дважды Esc чтобы вернуться в меню."""
LAST_NAME_INPUT = "Фамилия кириллицей: "
FIRST_NAME_INPUT = "Имя кириллицей: "
PATRONYMIC_INPUT = "Отчество кириллицей: "
ORGANIZATION_INPUT = "Название организации кириллица или латиница: "
WORK_PHONE_INPUT = "Рабочий телефон в формате +7(9XX)XXX-XX-XX: "
MOBILE_INPUT = "Мобильный телефон в формате +7(9XX)XXX-XX-XX: "
INDEX_INPUT = "Индекс записи: "
CONTACT_CREATED = "Контакт создан: {}"
CONTACT_UPDATED = "Контакт обновлен: {}"
CHOICE_INPUT = "Выберите номер пункта: "
SEARCH_INDEX = "Введите индекс записи, которую хотите изменить: "
ENTER_OR_ESC = "Введите поля, которые хотите изменить или Enter для пропуска."
INVALID_INDEX = "Неверный индекс."
SEARCH_RESULTS = "Результаты поиска:"
NOT_FOUND = "Ничего не найдено."
CHOOSE_1_TO_5 = "Пожалуйста, выберите пункт от 1 до 5."

# регулярные выражения для проверки вводимых значений
CYRILLIC_NAME_PATTERN = r'[а-яёА-ЯЁ-]+'
PHONE_PATTERN = r'\+7\(\d{3}\)\d{3}-\d{2}-\d{2}'
CYRILLIC_ORGANIZATION_PATTERN = r'[а-яёА-ЯЁ0-9]+'
LATIN_ORGANIZATION_PATTERN = r'[a-zA-Z0-9]+'
