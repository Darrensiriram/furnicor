import re
from typing import Optional, Union
from interface.IResponses import IResponse

class PostalCodeResponse(IResponse[str]):
    def __init__(self, name:Optional[str] = 'postalCode', prompt: Optional[str] = 'example: 3015CX: ')-> None:
        super().__init__(name,prompt)

    def _validate(self, value: str) -> Union[str, bool]:
        if re.search("^[1-9]{1}[0-9]{3}[A-Z]{2}$", value) is None:
            return (
                'PostalCode is not valid!'
                'Please see example: 3015CX '
            )

        return True
    def _sanitize(self, value: str) -> str:
        return value

