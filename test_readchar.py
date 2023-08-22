import readchar


def get_esc_key_code():
    print("Нажмите клавишу 'Esc' ...")
    key_bytes = readchar.readkey().encode()
    return key_bytes


def get_enter_key_code():
    print("Нажмите клавишу 'Enter' ...")
    key_bytes = readchar.readkey().encode()
    return key_bytes


esc_key_code = get_esc_key_code()
enter_key_code = get_enter_key_code()

print(f"Код клавиши 'Esc' в вашей системе: {esc_key_code}")
print(f"Код клавиши 'Enter' в вашей системе: {enter_key_code}")
