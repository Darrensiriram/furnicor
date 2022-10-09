import re
from typing import Optional, Union

from interface.IResponses import CorrectType, IResponse
from services.userService import UserService

class UsernameResponse(IResponse[str]):
    userS: UserService

    def __init__(self, userS: UserService, name: Optional[str] = 'username', prompt: Optional[str] = 'Username: ') -> None:
        super().__init__(name, prompt)
        self.userS = userS


    def _validate(self, value: str) -> Union[str, bool]:
        if re.search("^[a-zA-Z][a-zA-Z0-9_'.]{5,9}$", value) is None:
            return """
               The username is not valid!

               Usernames must meet the following requirements:
               - at least 6 characters
               - no longer than 10 characters
               - started with a letter
               - can only contain letters, numbers, underscores, apostrophes and periods
                       """
        if self.userS.checkIfUserExits(value.lower()):
            return 'User already exits!'
        return True

    def _sanitize(self, value: str) -> CorrectType:
        return value.lower()
