from typing import Any, Dict, List
from responses.passwordResponse import PasswordResponse
from responses.userResponse import UserResponse
from interface.IResponses import IResponse
from interface.IActions import IActions
from services.sessionService import SessionService
from services.userService import UserService

class SetTmpPasswordAction(IActions):
    session: SessionService
    userS: UserService

    def __init__(self, session:SessionService, userS: UserService):
        self.session = session
        self.userS = userS

    def is_actived(self) -> bool:
        return (
            self.session.loginCheck() and self.session.currentUser.role in ['system_administrator', 'super_admin']
        )
    def arguments(self) -> List[IResponse]:
        return [
            UserResponse(self.userS, access=True),
            PasswordResponse()
        ]
    def handle(self, arguments: Dict[str, Any]) -> None:
        self.userS.setTmpPwd(arguments['user'].id, arguments['password'])
        print("Temp pwd set!")
