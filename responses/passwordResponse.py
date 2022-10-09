import re
from typing import Optional, Union
from interface.IResponses import CorrectType, IResponse

class PasswordResponse(IResponse[str]):
    def __init__(self,  name: Optional[str] = 'password', prompt: Optional[str] = 'Password: ') -> None:
        super().__init__(name, prompt)


    def _validate(self, value: str) -> Union[str, bool]:
        if re.search('^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[^A-Za-z0-9]).{8,60}$', value) is None:
            return """
           The password is not valid!.

           Passwords must meet the following requirements:
           - at least 8 characters
           - at most 60 characters
           - must have a combination of at least one lowercase, one uppercase, one special character and one digit
                   """

        return True

    def _sanitize(self, value: str) -> CorrectType:
        return value