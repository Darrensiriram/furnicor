from typing import Any, Dict, List
from interface.IActions import IActions
from interface.IResponses import IResponse
from services.sessionService import SessionService
from responses.emptyResponse import EmptyResponse
from responses.passwordResponse import PasswordResponse
from services.userService import UserService

class UpdatePasswordAction(IActions):
    session: SessionService
    userS: UserService

    def __init__(self, session: SessionService, userS: UserService):
        self.session = session
        self.userS = userS

    def is_actived(self) -> bool:
        return self.session.loginCheck()

    def arguments(self) -> List[IResponse]:
        return [
            EmptyResponse('old_pw', 'old Password: '),
            PasswordResponse('new_pw', 'New Password: '),
            PasswordResponse('new_pw_confirm', 'Confirm new password: ')
        ]
    def handle(self, arguments: Dict[str, Any]) -> None:
        if arguments['new_pw'] != arguments['new_pw_confirm']:
            print('These password are not identical, change them please.')
            return

        try:
            self.userS.update_pwd(
                self.session.currentUser.id,
                arguments['old_pw'],
                arguments['new_pw'],
            )
            print('Successfully updated your password.')
        except ValueError:
            print('The entered old password is not correct.')
