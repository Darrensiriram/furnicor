from typing import Any, Dict, List
from interface.IActions import IActions
from interface.IResponses import IResponse
from services.sessionService import SessionService

class LogoutAction(IActions):
    session : SessionService
    def __init__(self, session: SessionService) -> None:
        self.session = session

    def is_actived(self) -> bool:
        return self.session.loginCheck()

    def arguments(self) -> List[IResponse]:
        return []

    def handle(self, arguments: Dict[str, Any]) -> None:
        self.session.closeSession()
        print("Logged out.")