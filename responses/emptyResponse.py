from typing import Union
from interface.IResponses import IResponse

class EmptyResponse(IResponse[str]):
    """Defines a string argument that may not be empty."""

    def _validate(self, value: str) -> Union[str, bool]:
        if len(value) == 0:
            return f'Argument {self.get_name()} is required.'

        return True


    def _sanitize(self, value: str) -> str:
        return value
