from typing import Optional
from interface.IEncryption import IEncryption

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABETWITHUPPER = ALPHABET + ALPHABET.upper()

class CeasarEncryption(IEncryption):
    __key: str

    def __init__(self, key: str) -> None:
        """Construct the Vigenere Crypto class.

        Make sure the key is lowercase and only contains a-z characters."""
        self.__key = key

    def encrypt(self, data: Optional[str]) -> Optional[str]:
        """Encrypts the given string using Vigenere and returns it."""
        if data is None:
            return None

        curr_key_index = 0
        encrypted = ''
        for _, char in enumerate(data):
            # Only encrypt a-zA-Z chars
            if char not in ALPHABETWITHUPPER:
                encrypted += char
                continue

            # The index of the current char in the key, so a = 0, b = 1, c = 2 etc.
            shift_by = ALPHABET.index(self.__key[curr_key_index % len(self.__key)])

            # Add the index of the curr char to the keys index and keep it in the alphabet length
            shifted = (ALPHABET.index(char.lower()) + shift_by) % len(ALPHABET)

            # Uppercase if the char was uppercase
            encrypted += ALPHABET[shifted].upper() if char.isupper() else ALPHABET[shifted]

            # Shift the index of the key by 1
            curr_key_index += 1
        return encrypted

    def decrypt(self, data: Optional[str]) -> Optional[str]:
        """Decrypts the string using the Vigenere cypher and returns it."""
        if data is None:
            return None

        curr_key_index = 0
        decrypted = ''
        for _, char in enumerate(data):
            # Only decrypt a-zA-Z chars
            if char not in ALPHABETWITHUPPER:
                decrypted += char
                continue

            # The index of the current char in the key, so a = 0, b = 1, c = 2 etc.
            shifted_by = ALPHABET.index(self.__key[curr_key_index % len(self.__key)])

            # Subtract the index of the curr char
            # to the keys index and keep it in the alphabet length
            unshifted = (ALPHABET.index(char.lower()) - shifted_by) % len(ALPHABET)

            # Uppercase if the char was uppercase
            decrypted += ALPHABET[unshifted].upper() if char.isupper() else ALPHABET[unshifted]

            # Shift the index of the key by 1
            curr_key_index += 1
        return decrypted