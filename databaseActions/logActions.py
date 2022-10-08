from contextlib import suppress
from sqlite3.dbapi2 import Connection
from typing import Any,Dict,List

from interface.IEncryption import IEncryption
from model.user import User
from model.log import Log
from interface.IDatabaseActions import IDatabaseActions


class LogActions(IDatabaseActions[Log]):

    userAction = IDatabaseActions[User]

    def allowedColumns(self) -> List[str]:
        return [
            'id',
            'user_id',
            'is_supicious',
            'message',
            'created_at',
            'seen_by'
        ]
    def encryptColumns(self) -> List[str]:
        return ['message']

    def __init__(self, connection: Connection, cipher: IEncryption, userAction: IDatabaseActions[User]) -> None:
        super().__int__(connection, cipher)
        self.userAction = userAction


    def selectAll(self) -> List[Log]:
        sql = self.connection.execute('SELECT * FROM logs ORDER BY created_at ASC').fetchall()
        return [self.decryptTuple(value) for value in sql]

    def selectOne(self, Id: int) -> Log:
        sql = self.connection.execute('select * FROM logs WHERE id = ?' (Id)).fetchone()
        if not sql:
            raise Exception(f"No log found with Id: {Id}")
        return self.decryptTuple(sql)

    def where(self, criteria:Dict[str,str]) -> List[Log]:
        result = self.findModel('logs',criteria)
        return [self.decryptTuple(result) for r in result]

    def update(self, id: int, updates:Dict[str, Any]):
        return self.updateModel('logs', id, updates)

    def create(self, model: Log) -> None:
        encryptModel = self.encrypt(model)
        self.connection.execute(
            'INSERT INTO logs VALUES (?,?,?,?,?)',
            tuple(encryptModel.values())
        )
        self.connection.commit()

    def delete(self, id: int) -> None:
        self.connection.execute('DELETE FROM logs WHERE id = ?', id)
        self.connection.commit()

    def createTable(self) -> None:
        self.connection.execute(
            'CREATE TABLE IF NOT EXISTS logs('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'message VARCHAR NOT NULL,'
            'is_suspicious TINYINT NOT NULL,'
            'user_id INTEGER,'
            'created_at TIMESTAMP NOT NULL,'
            ')'
        )


    def encrypt(self, log: Log) -> Dict:
        return {
            'id' : log.id,
            'message': self.cipher.encrypt(log.message),
            'is_suspicious': log.is_suspicious,
            'user_id': None if log.user is None else Log.user.id,
            'created_at': log.created_at,
        }

    def decrypt(self, data: Dict) -> Log:
        user = None
        with suppress(NameError):
            user = self.userAction.selectOne(data['user_id'])

        return Log(
            str(self.cipher.decrypt(data['message'])),
            user,
            data['id'],
            data['is_suspicious'] == 1,
            data['created_at'],
        )

    def decryptTuple(self, data:tuple) -> Log:
        return self.decrypt({
            'id': data[0],
            'message': data[1],
            'is_suspicious': data[2],
            'user_id': data[3],
            'created_at': data[4],
        })