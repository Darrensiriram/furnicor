import re
from typing import Optional, Union

from interface.IResponses import IResponse

class EmailResponse(IResponse[str]):

    def __init__(self,  name: Optional[str] = 'email',prompt: Optional[str] = 'Email: ') -> None:
        super().__init__(name,prompt)

    def _validate(self, value: str) -> Union[str, bool]:
        if re.search(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', value) is None:
            return 'This is not a valid email.'
        return True

    def _sanitize(self, value: str) -> str:
        return value

