from typing import Any, Dict, List


from responses. userResponse import UserResponse

from interface.IResponses import IResponse
from interface.IActions import IActions

from services.userService import UserService
from services.sessionService import SessionService

class DeleteUserAction(IActions):
    session: SessionService
    userS: UserService

    def __init__(self, session: SessionService, userS: UserService) -> None:
        self.session = session
        self.userS = userS

    def is_actived(self) -> bool:
        return (
            self.session.loginCheck() and self.session.currentUser.role in ['system_administrator', 'super_admin']
        )
    def arguments(self) -> List[IResponse]:
        return [UserResponse(self.userS, access=True)]

    def handle(self, arguments: Dict[str, Any]) -> None:
        self.userS.delete(arguments['user'].id)
        print('User deleted!')



