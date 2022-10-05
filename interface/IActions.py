from abc import ABC, abstractmethod
from typing import Any, Dict, List
from interface.iArgument import IArgument

class IActions(ABC):
    """Actions are made here"""
    @abstractmethod
    def is_actived(self) -> bool:
        """Check if a command is actived"""

    @abstractmethod
    def arguments(self) -> List[IArgument]:
        """Return a list of all arguments that can perfom that action"""

    @abstractmethod
    def handle(self, arguments: Dict[str, Any]) -> None:
        """Check for the request"""