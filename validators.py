import re

from constants import (CYRILLIC_NAME_PATTERN, CYRILLIC_ORGANIZATION_PATTERN,
                       LATIN_ORGANIZATION_PATTERN, PHONE_PATTERN)


def validate_name_cyrillic(name):
    """
    Функция проверяет фамилию, имя или отчество на соответствие
    регулярному выражению. Допустимы только русские буквы.
    Длина имени должна быть больше 2 символов.
    """
    if len(name) < 2:
        return False
    if re.fullmatch(CYRILLIC_NAME_PATTERN, name):
        return True
    return False


def validate_phone(mobile_phone):
    """
    Функция проверяет телефон на соответствие
    регулярному выражению. Номер телефона должен быть
    в формате: +7(9XX)XXX-XX-XX.
    """
    return re.fullmatch(PHONE_PATTERN, mobile_phone)


def validate_organization(organization):
    """
    Функция проверяет название организации на соответствие
    регулярному выражению.
    Допустимы либо только буквы русского, либо латинского алфавита.
    Длина названия должна быть больше 2 символов.
    """
    if len(organization) < 2:
        return False
    return re.fullmatch(
        LATIN_ORGANIZATION_PATTERN, organization) or re.match(
            CYRILLIC_ORGANIZATION_PATTERN, organization)
