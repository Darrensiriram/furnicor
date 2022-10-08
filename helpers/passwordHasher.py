from base64 import b64decode, b64encode
from hashlib import scrypt
from os import urandom
from typing import Tuple

class PasswordHasher():

    @classmethod
    def hashPw(cls, password: str, salt: bytes = urandom(10)) -> Tuple[str,str]:
        """Hash the password"""
        hash = scrypt(password.encode('UTf-8'), salt=salt, n=2, r=8, p=1)
        return b64encode(hash).decode('UTF-8'), b64encode(salt).encode('UTF-8')

    def checkHashedPw(cls, password:str, hashedPw: str, salt:str) -> bool:
        try:
            hashToverify = cls.hashPw(password, b64encode(salt.encode('UTF-8')))
            if hashToverify == hashedPw: return True
        except:
            return False
