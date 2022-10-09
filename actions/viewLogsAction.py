from typing import Any, Dict, List
from interface.IResponses import IResponse
from interface.IActions import IActions
from helpers.initializer import showLogs
from services.logService import LogService
from services.sessionService import SessionService

class ViewLogsAction(IActions):
    session: SessionService
    log: LogService

    def __init__(self, session: SessionService, log: LogService) -> None:
        self.session = session
        self.log = log

    def is_actived(self) -> bool:
        return(
            self.session.loginCheck() and self.session.currentUser.role in ['system_administrator', 'super_admin']
        )
    def arguments(self) -> List[IResponse]:
        return []
    def handle(self, arguments: Dict[str, Any]) -> None:
        log = self.log.selectAllLogs()
        showLogs(log)
