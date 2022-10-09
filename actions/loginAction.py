from typing import Any, Dict, List
from interface.IActions import IActions
from interface.IResponses import IResponse
from services.sessionService import SessionService
from services.userService import UserService
from services.logService import LogService
from responses.emptyResponse import EmptyResponse

class LoginAction(IActions):
    session: SessionService
    log: LogService
    userS: UserService

    def __init__(self, session: SessionService, log: LogService, userS: UserService )-> None:
        self.session = session
        self.userS = userS
        self.log = log

    def is_actived(self) -> bool:
        return not self.session.loginCheck()

    def arguments(self) -> List[IResponse]:
        return [
            EmptyResponse('username', 'Username: '),
            EmptyResponse('password', 'Password: '),
        ]
    def handle(self, arguments: Dict[str, Any]) -> None:
        valid = self.userS.login(arguments['username'], arguments['password'])
        if valid is False:
            print("Errrr! login failed!")
            return

        print("Yeey! ur logged in!")

        if self.session.currentUser.has_temp_password:
            print("Your password has been set by a other user. please change your password ASAP!")