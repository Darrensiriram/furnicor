from abc import ABC, abstractmethod


class IModel(ABC):
    @abstractmethod
    def getId(self) -> int:
        """retuns ID"""
