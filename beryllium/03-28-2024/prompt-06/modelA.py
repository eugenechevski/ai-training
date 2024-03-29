def basic_encryption(string, shift_amount):
    # Convert the shift amount to an integer to avoid issues with floats or other non-integer values
    shift_amount = int(shift_amount)

    # Create a new string to store the encrypted result
    encrypted_string = ""

    # Iterate through each character in the input string
    for char in string:
        # Check if the character is an alphabetical letter (upper or lower case)
        if char.isalpha():
            # Convert the character to an ASCII code
            ascii_code = ord(char)

            # Apply the shift to the ASCII code and ensure it remains within the valid range of alphabetical characters (65-90 for uppercase, 97-122 for lowercase)
            if char.isupper():
                shifted_ascii_code = (ascii_code - 65 + shift_amount) % 26 + 65
            else:
                shifted_ascii_code = (ascii_code - 97 + shift_amount) % 26 + 97

            # Convert the shifted ASCII code back to a character and append it to the encrypted string
            encrypted_string += chr(shifted_ascii_code)
        else:
            # If the character is not an alphabetical letter, append it to the encrypted string as it is
            encrypted_string += char

    # Return the encrypted string
    return encrypted_string

# Test the basic_encryption function with a sample string and shift amount
original_string = "Hello, World!"
shift_amount = 5
encrypted_string = basic_encryption(original_string, shift_amount)
print("Original string:", original_string)
print("Encrypted string:", encrypted_string)