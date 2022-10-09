from typing import Any, Dict, List
from responses.emptyResponse import EmptyResponse
from responses.selectResponse import SelectResponse
from responses.selectMoreResponses import SelectMoreResponses
from responses. userResponse import UserResponse
from responses.usernameResponse import UsernameResponse

from interface.IResponses import IResponse
from interface.IActions import IActions
from services.userService import UserService
from services.sessionService import SessionService
from helpers.initializer import ShowUsers


class UpdateUserAction(IActions):

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
        return [
            UserResponse(self.userS, access=True),
            SelectMoreResponses(
                'updateCol',
                'Select column to update: ',
                'updating the user..... ',{
                    'username': 'Username',
                    'first_name': 'First name',
                    'last_name' : 'Last name',
                    'role': 'Role'
                }
            )
        ]

    def handle(self, arguments: Dict[str, Any]) -> None:
        columnUpdate = arguments['updateCol']
        user = arguments['user']

        updates ={}

        if 'username' in columnUpdate:
            updates['username'] = UsernameResponse(self.userS).ask()
        if 'first_name' in columnUpdate:
            updates['first_name'] = EmptyResponse('first_name', 'First name: ').ask()
        if 'last_name' in columnUpdate:
            updates['last_name'] = EmptyResponse('last_name', 'Last name: ').ask()
        if 'role' in columnUpdate:
            choices = {'advisor': 'Advisor'}
            if self.session.currentUser.role == 'super_admin':
                choices['system_administator'] = 'System administrator'

            updates['role'] = SelectResponse('role', 'Role: ', choices).ask()

        updated = self.userS.update(user.id, updates)

        print("User has been Updated")
        ShowUsers([updated])