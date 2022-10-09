from typing import Callable, Dict, List, Tuple
from model.log import Log
from databaseActions.logActions import LogActions
from sessionService import SessionService

class LogService():
    session: SessionService
    action: LogActions
    attempts: Dict[str, tuple[Callable[[int],str], int, int]]

    def __init__(self, session: SessionService, action: LogActions):
        self.session = session
        self.action = action
        self.attempts = {}

    def logInfo(self,message:str):
        currentLoggedInUser = self.session.currentUser if self.session.loginCheck() else None
        log = Log(message, user=currentLoggedInUser)
        self.action.create(log)

    def logFraud(self, message: str):
        currentLoggedInUser = self.session.currentUser if self.session.loginCheck() else None
        log = Log(message, is_suspicious=True, user=currentLoggedInUser)
        self.action.create(log)

    def selectAllLogs(self) -> List[Log]:
        return self.action.selectAll()
