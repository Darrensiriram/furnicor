"""Holds the ICommand abstract class."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List

from iargument import IArgument

class ICommand(ABC):
    """A command defines an action in the system."""

    @abstractmethod
    def is_enabled(self) -> bool:
        """Whether to allow the user to execute this command."""

    @abstractmethod
    def arguments(self) -> List[IArgument]:
        """Returns a list of all arguments required to perform the action."""

    @abstractmethod
    def handle(self, arguments: Dict[str, Any]) -> None:
        """Handles the request, arguments are already validated here."""
