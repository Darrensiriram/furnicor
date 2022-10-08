from abc import ABC, abstractmethod
from typing import Optional


class IEncryption(ABC):

    @abstractmethod
    def encrypt(self, data: Optional[str]) -> Optional[str]:
        """Encrypt the string"""

    def decrypt(self, data: Optional[str]) -> Optional[str]:
        """Decrypt the string"""
