def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha(): #check if the character is a letter
            shift_base = 65 if char.isupper() else 97 # if Uppercase = 65 or for Lowercase = 97
            # shift the character based on it case and modulo by 26 to wrap around
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base )
        else:
            #IF not a letter then just add as it is
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift) # reuse the function with negative shift


def main():
    choice = input("Would you like to encrypt or decrypt? (e/d): ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        encrypted_message = caesar_encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == 'd':
        decrypted_message = caesar_decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid Choice, please enter e or d.")


main()