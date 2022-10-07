from typing import Optional
from interface.IEncryption import IEncryption

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

class CeasarEncryption(IEncryption):

    plaintText: str

    def __int__(self, plainText: str) -> None:
        self.plaintText = plainText


    def encrypt(self, data: Optional[str]) -> Optional[str]:
        if data is None: return None

        encrypt_ceasar = ''
        shift = 4

        for i in self.plaintText:
            if i in alphabet:
                position = alphabet.find(i)
                new_position = (position + shift) % 26
                new_character = alphabet[new_position]
                if i.isupper():
                    new_character = new_character.upper()
                encrypt_ceasar += new_character
            else:
                encrypt_ceasar += i

        return encrypt_ceasar

    def decrypt(self, data: Optional[str]) -> Optional[str]:
        if data is None: return None

        decrypt_caesar = ''
        shift = 4

        for i in self.plaintText:
            if i in alphabet:
                position = alphabet.find(i)
                new_position = (position - shift) % 26
                new_character = alphabet[new_position]
                if i.isupper():
                    new_character = new_character.upper()
                decrypt_caesar += new_character
            else:
                decrypt_caesar += i
        result = str(decrypt_caesar)

        return result