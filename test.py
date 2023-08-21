import readchar

def get_esc_key_code():
    print("Press the 'Esc' key...")
    key_bytes = readchar.readkey().encode()
    return key_bytes

esc_key_code = get_esc_key_code()
print(f"The 'Esc' key code on your system is: {esc_key_code}")