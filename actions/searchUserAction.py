from typing import Any, Dict, List
from interface.IActions import IActions
from interface.IResponses import IResponse
from helpers.initializer import ShowUsers
from services.sessionService import SessionService
from services.userService import UserService
from responses.emptyResponse import EmptyResponse

class SearchUserAction(IActions):
    session: SessionService
    userS: UserService

    def __init__(self, session: SessionService, userS: UserService):
        self.session = session
        self.userS = userS

    def is_actived(self) -> bool:
        return (
                self.session.loginCheck() and self.session.currentUser.role in ['system_administrator', 'super_admin']
        )

    def arguments(self) -> List[IResponse]:
        return [
            EmptyResponse('criteria', 'Search criteria: ')
        ]
    def handle(self, arguments: Dict[str, Any]) -> None:
        user = self.userS.search(arguments['criteria'])
        ShowUsers(user)