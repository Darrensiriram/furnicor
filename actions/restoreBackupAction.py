from typing import Any, Dict, List
from responses.selectResponse import SelectResponse
from interface.IActions import IActions
from interface.IResponses import IResponse
from services.backupService import BackUpService
from services.sessionService import SessionService

class RestoreBackupAction(IActions):
    session: SessionService
    backupS: BackUpService

    def __init__(self, session: SessionService, backupS: BackUpService) -> None:
        self.session = session
        self.backupS = backupS

    def is_actived(self) -> bool:
        return (
            self.session.loginCheck() and self.session.currentUser.role in ['system_administrator', 'super_admin']
        )
    def arguments(self) -> List[IResponse]:
        return []
    def handle(self, arguments: Dict[str, Any]) -> None:
        allBackups = self.backupS.checkAllBackups()
        backupDict= {}

        for i, backup in enumerate(backupDict):
            backupDict[i] = backup

        backup = SelectResponse('Backup', 'Select the backup restored: ', backupDict).ask()
        backup = backupDict[backup]

        self.backupS.restore(backup)
        print('Backup has been restored. ')
