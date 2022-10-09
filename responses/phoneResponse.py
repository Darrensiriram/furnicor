from typing import Optional, Union
from interface.IResponses import IResponse

class PhoneResponse(IResponse[str]):
    def __init__(self, name: Optional[str] = 'phone',prompt: Optional[str] = 'Phone number: ') -> None:
        super().__init__(name, prompt)

    def _validate(self, value: str) -> Union[str, bool]:
        if value.isdigit() and len(value) == 8:
            return True

        return (
            'Your input is not a valid number, '
            'it should only contain digits and be 8 characters long.'
        )
    def _sanitize(self, value: str) -> str:
        return  value