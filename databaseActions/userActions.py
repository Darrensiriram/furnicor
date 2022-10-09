from typing import Any, Dict, List
from model.user import User
from interface.IDatabaseActions import IDatabaseActions


class UserActions(IDatabaseActions[User]):

    @property
    def allowedColumns(self) -> List[str]:
        return [
            'id',
            'username',
            'first_name',
            'last_name',
            'created_at',
            'password',
            'salt',
            'role',
            'has_temp_password',
        ]

    @property
    def encryptColumns(self) -> List[str]:
        return ['first_name', 'last_name']

    def selectAll(self) -> List[User]:
        sql = self.connection.execute('SELECT * FROM user').fetchall()
        return [self.decryptTuple(value) for value in sql]

    def selectOne(self, Id: int) -> User:
        sql = self.connection.execute('SELECT * FROM user WHERE id = ?', (Id,)).fetchone()
        if not sql:
            raise Exception(f"No user found with Id: {Id}")
        return self.decryptTuple(sql)

    def create(self, model: User) -> None:
        encryptedValue = self.encrypt(model)
        self.connection.execute('INSERT INTO user VALUES (?,?,?,?,?,?,?,?,?)', tuple(encryptedValue.values()))
        self.connection.commit()

    def createTable(self) -> None:
        self.connection.execute((
            'CREATE TABLE IF NOT EXISTS user('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'username VARCHAR NOT NULL,'
            'first_name VARCHAR NOT NULL,'
            'last_name VARCHAR NOT NULL,'
            'role VARCHAR NOT NULL,'
            'password VARCHAR NOT NULL,'
            'salt VARCHAR NOT NULL,'
            'created_at TIMESTAMP NOT NULL,'
            'has_temp_password INT NOT NULL'
            ')'
        ))
        self.connection.commit()

    def delete(self, id: int) -> None:
        sql = self.connection.execute('DELETE * FROM user WHERE id = ?', id)
        self.connection.commit()

    def update(self, id: int, updates: Dict[str, Any]) -> User:
        return self.updateModel('user', id, updates)

    def where(self, criteria: Dict[str, str]) -> List[User]:
        results = self.findModel('user', criteria)
        return [self.decryptTuple(result) for result in results]

    def encrypt(self, user: User) -> Dict:
        return {
            'id': user.id,
            'username': user.username,
            'first_name': self.cipher.encrypt(user.first_name),
            'last_name': self.cipher.encrypt(user.last_name),
            'role': user.role,
            'password': user.password,
            'salt': user.salt,
            'created_at': user.created_at,
            'has_temp_password': user.has_temp_password,
        }

    def decrypt(self, data: Dict) -> User:
        return User(
            data['username'],
            self.cipher.decrypt(data['first_name']),
            self.cipher.decrypt(data['last_name']),
            data['role'],
            data['password'],
            data['salt'],
            data['id'],
            data['created_at'],
            data['has_temp_password'] == 1,
        )

    def decryptTuple(self, data: tuple) -> User:
        return self.decrypt({
            'id': data[0],
            'username': data[1],
            'first_name': data[2],
            'last_name': data[3],
            'role': data[4],
            'password': data[5],
            'salt': data[6],
            'created_at': data[7],
            'has_temp_password': data[8],
        })
