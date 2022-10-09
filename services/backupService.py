import os
from os import path
import shutil
from datetime import datetime
from typing import List
from services.logService import LogService

class BackUpService:
    path: str
    log: LogService

    def __init__(self, path: str, log:LogService):
        self.path = path
        self.log = log


    def backup(self) -> str:

        if not path.exists('../backups'):
            os.makedirs('../backups')
        else:
            filename = datetime.now().strftime('%d-%m-%Y-%H-%M-%S')
            filepath = shutil.make_archive('backup', 'zip', f'{self.path}/data')
            destination = shutil.move(filepath, f'{self.path}/backups/{filename}.zip')

        self.log.logInfo(f'backup made: {filename}.')

        return destination

    def restore(self, filename:str) -> None:
        filepath = f'{self.path}/backups/{filename}.zip'
        shutil.unpack_archive(filepath, f'{self.path}/data')

        self.log.logInfo(f'Restored the backup from {filename}.')

    def checkAllBackups(self) -> List[str]:

        entries = os.listdir(f'{self.path}/backups')
        backups = [file.removesuffix('.zip') for file in entries if file.endswith('.zip')]
        self.log.logInfo(f'Retrieved backups, got {len(backups)} results.')
        return backups
