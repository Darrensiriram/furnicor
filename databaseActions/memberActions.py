from typing import Any, Dict, List
from model.member import Member
from interface.IDatabaseActions import IDatabaseActions


class MemberActions(IDatabaseActions[Member]):
    """Database actions for the member table"""

    def allowedColumns(self) -> List[str]:
        return ['id', 'first_name', 'last_name', 'street_name', 'house_number', 'postalCode', 'city', 'email', 'phone',
                'created_at']

    def encryptColumns(self) -> List[str]:
        return ['first_name', 'last_name', 'street_name', 'house_number', 'postalCode', 'city', 'email', 'phone']

    def selectAll(self) -> List[Member]:
        sql = self.connection.execute('SELECT * FROM members').fetchall()
        return [self.decryptTuple(v) for v in sql]

    def selectOne(self, Id: int) -> List[Member]:
        sql = self.connection.execute('SELECT * FROM members WHERE id = ?', (Id)).fetchone()
        if not sql:
            raise Exception(f"No member found with Id: {Id}")
        return self.decryptTuple(sql)

    def create(self, model: Member) -> None:
        encryptedResult = self.encrypt(model)
        self.connection.execute('INSERT INTO members VALUES (?,?,?,?,?,?,?,?,?,?)', tuple(encryptedResult.values()))
        self.connection.commit()

    def delete(self, id: int) -> None:
        self.connection.execute('DELETE FROM members WHERE id = ?', id)
        self.connection.commit()

    def createTable(self) -> None:
        self.connection.execute((
            'CREATE TABLE IF NOT EXISTS members('
            'id INTEGER PRIMARY KEY NOT NULL,'
            'first_name VARCHAR NOT NULL,'
            'last_name VARCHAR NOT NULL,'
            'street_name VARCHAR NOT NULL,'
            'house_number VARCHAR NOT NULL,'
            'postalCode VARCHAR NOT NULL,'
            'city VARCHAR NOT NULL,'
            'email VARCHAR NOT NULL,'
            'phone VARCHAR NOT NULL,'
            'created_at TIMESTAMP NOT NULL'
            ')'
        ))
        self.connection.commit()

    def update(self, id: int, updates: Dict[str, Any]) -> Member:
        return self.updateModel('members', id, updates)

    def where(self, criteria:Dict[str,str]) -> List[Member]:
        results = self.findModel('member', criteria)
        return [self.decryptTuple(result) for result in results]

    def encrypt(self, member: Member) -> Dict:
        return {
            'id': member.id,
            'first_name': self.cipher.encrypt(member.first_name),
            'last_name': self.cipher.encrypt(member.last_name),
            'street_name': self.cipher.encrypt(member.street_name),
            'house_number': self.cipher.encrypt(member.house_number),
            'postalCode': self.cipher.encrypt(member.postalCode),
            'city': self.cipher.encrypt(member.city),
            'email': self.cipher.encrypt(member.email),
            'phone': self.cipher.encrypt(member.phone),
            'created_at': member.created_at
        }

    def decrypt(self, data: Dict) -> Member:
        return Member(
            data['id'],
            self.cipher.decrypt(data['first_name']),
            self.cipher.decrypt(data['last_name']),
            self.cipher.decrypt(data['street_name']),
            self.cipher.decrypt(data['house_number']),
            self.cipher.decrypt(data['zip_code']),
            self.cipher.decrypt(data['city']),
            self.cipher.decrypt(data['email']),
            self.cipher.decrypt(data['phone']),
            data['created_at']
        )

    def decryptTuple(self, data: tuple) -> Member:
        return self.decrypt({
            'id': data[0],
            'first_name': data[1],
            'last_name': data[2],
            'street_name': data[3],
            'house_number': data[4],
            'zip_code': data[5],
            'city': data[6],
            'email': data[7],
            'phone': data[8],
            'created_at': data[9],
        })
