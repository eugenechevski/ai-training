def encrypt(plain_text, shift):
    if not isinstance(plain_text, str) or not all(c.isalpha() for c in plain_text):
        raise ValueError(
            "Input must be a string containing only alphabetical characters.")
    if shift < 0 or shift > 25:
        raise ValueError("Shift value must be between 0 and 25.")

    cipher_text = ""
    for c in plain_text:
        if c.isupper():
            cipher_char = chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        else:
            cipher_char = chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        cipher_text += cipher_char

    return cipher_text


try:
    cipher_text = encrypt("HelloWorld", 3)
    print(cipher_text)
except ValueError as e:
    print(e)
