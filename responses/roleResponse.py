from typing import Dict, Optional, Union
from services.sessionService import SessionService
from responses.selectResponse import SelectResponse

class RoleResponse(SelectResponse[str]):
    session: SessionService

    def __init__(self, session: SessionService, name: str = 'role', prompt: str = 'Role: ', choices: Optional[Dict[str,str]] = None) -> None:
        if choices is None:
            choices = {
                'advisor': 'Advisor',
                'system_administrator': 'Sytem administrator'
            }
            super().__init__(name,prompt,choices)
            self.session = session


    def _validate(self, value: str) -> Union[str, bool]:
        value = self.valueTokey(value)
        if self.session.currentUser.role == 'super_admin':
            return True
        if self.session.currentUser.role == 'advisor':
            return 'Oops! ur not allowed to create a user because you are an advisor'
        if self.session.currentUser == 'system_administrator' and value != 'advisor':
            return 'Only admin are allowed to make users'
        return True
