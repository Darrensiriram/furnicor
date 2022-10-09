from typing import Any, Dict, List
from responses.passwordResponse import PasswordResponse
from responses.roleResponse import RoleResponse
from responses.usernameResponse import UsernameResponse
from responses.emptyResponse import EmptyResponse
from interface.IActions import IActions
from interface.IResponses import IResponse
from services.sessionService import SessionService
from services.userService import UserService

class CreateUserAction(IActions):
    session: SessionService
    userS: UserService

    def __init__(self, session: SessionService, userS: UserService) -> None:
        self.session = session
        self.userS = userS

    def is_actived(self) -> bool:
        return(
            self.session.loginCheck() and self.session.currentUser.role in ['system_administrator', 'super_admin']
        )
    def arguments(self) -> List[IResponse]:
        return[
            UsernameResponse(self.userS),
            PasswordResponse(),
            EmptyResponse('first_name', 'First name: '),
            EmptyResponse('last_name', 'Last name: '),
            RoleResponse(self.session)
        ]
    def handle(self, arguments: Dict[str, Any]) -> None:
        user = self.userS.createUser(
            arguments['username'],
            arguments['first_name'],
            arguments['last_name'],
            arguments['role'],
            arguments['password'],
        )
        print(f'User created! Welcome: {user.first_name}')
