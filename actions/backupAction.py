from typing import Any, List, Dict
from interface.IResponses import IResponse
from interface.IActions import IActions
from services.backupService import BackUpService
from services.sessionService import SessionService


class BackupAction(IActions):
    __session: SessionService
    __backupS: BackUpService

    def __init__(self, session: SessionService, backupS: BackUpService):
        self.__session = session
        self.__backupS = backupS

    def is_actived(self) -> bool:
        return (
                self.__session.loginCheck() and self.__session.currentUser.role in ['system_administrator',
                                                                                    'super_admin']
        )

    def arguments(self) -> List[IResponse]:
        return []

    def handle(self, arguments: Dict[str, Any]) -> None:
        backupAction = self.__backupS.backup()
        print(f'Backup generated: {backupAction}')
