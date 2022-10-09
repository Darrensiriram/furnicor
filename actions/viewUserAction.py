from typing import Any, Dict, List
from interface.IResponses import IResponse
from interface.IActions import IActions
from helpers.initializer import ShowUsers
from services.sessionService import SessionService
from services.userService import UserService


class ViewUserAction(IActions):
    userS: UserService
    session: SessionService

    def __init__(self, session: SessionService, userS: UserService) -> None:
        self.userS = userS
        self.session = session

    def is_actived(self) -> bool:
        return (
                self.session.loginCheck() and self.session.currentUser.role in ['system_administrator', 'super_admin']
        )

    def arguments(self) -> List[IResponse]:
        return []

    def handle(self, arguments: Dict[str, Any]) -> None:
        usr = self.userS.showAllUsers()
        ShowUsers(usr)
