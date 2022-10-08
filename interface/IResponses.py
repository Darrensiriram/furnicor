from abc import abstractmethod
from typing import Generic, Optional, TypeVar, Union

from interface.Quit import Quit

CorrectType = TypeVar('CorrectType')

class IResponse(Generic[CorrectType]):
    """Defines an argument."""

    _prompt: str
    _name: str

    def __init__(self, name: str, prompt: str) -> None:
        self._prompt = prompt
        self._name = name

    @abstractmethod
    def _validate(self, value: str) -> Union[str, bool]:
        """Validate an argument"""

    @abstractmethod
    def _sanitize(self, value: str) -> CorrectType:
        """Sanitize the value and cast it to the desired type."""

    def ask(self) -> CorrectType:
        """Asks the user for the argument."""

        user_input: Optional[str] = None
        while True:
            user_input = input(self._prompt)
            if user_input in ['q', 'quit']:
                raise Quit()

            validated = self._validate(user_input)
            if isinstance(validated, str):
                print(validated)
                continue

            if validated is False:
                print(f'Invalid value for argument {self.get_name()}, try again.')
                continue

            break

        return self._sanitize(user_input)

    def get_name(self) -> str:
        """Returns the argument name."""
        return self._name
