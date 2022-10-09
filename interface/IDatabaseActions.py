from abc import abstractmethod
from sqlite3 import Connection
from typing import Any, Dict, Generic, List, Tuple, TypeVar

from interface.IEncryption import IEncryption

CorrectType = TypeVar('CorrectType')
class IDatabaseActions(Generic[CorrectType]):
    connection: Connection
    cipher: IEncryption

    def __init__(self, connection: Connection, cipher: IEncryption) -> None:
        self.connection = connection
        self.cipher = cipher
        self.createTable()

    @abstractmethod
    def createTable(self) -> None:
        """Create the table inside the database"""
    @abstractmethod
    def delete(self, id: int)-> None:
        """Deletes the model with the given ID"""
    @abstractmethod
    def create(self, model: CorrectType) -> None:
        """Create the model"""
    @abstractmethod
    def update(self, id: int, updates:Dict[str, Any]):
        """Updates the model With the given ID"""
    @abstractmethod
    def where(self, criteria:Dict[str,str]) -> List[CorrectType]:
        """Defines the search criteria and return a list of models"""
    @abstractmethod
    def selectAll(self) -> List[CorrectType]:
        """Return all the records of the model"""
    @abstractmethod
    def selectOne(self, Id: int) -> CorrectType:
        """Return one selected model chosen by Id"""

    @abstractmethod
    def allowedColumns(self)-> List[str]:
        """check if you can search in certain columns"""
    @abstractmethod
    def encryptColumns(self) -> List[str]:
        """check if column need to be encrypted"""


    def updateModel(self, table:str, Id:int, updates: Dict[str, Any]) -> CorrectType:
        if len(updates) == 0:
            return self.selectOne(Id)

        updateCriteria = ', '.join([f'{item[0]} = ?' for item in updates.items()])

        prepared = tuple()

        for k, v in updates.items():
            print(k)
            if k not in self.allowedColumns:
                raise Exception("Not a valid column ")

            prepared = prepared + (
                (self.cipher.encrypt(v) if k in self.encryptColumns else v),
            )

            prepared = prepared + (Id, )
        print(updateCriteria)
        self.connection.execute(f'UPDATE {table} SET {updateCriteria} WHERE id = ?', prepared)
        self.connection.commit()

        return self.selectOne(Id)


    def findModel(self, table: str, criteria: Dict[str, Any]) -> List[Tuple]:
        if len(criteria) == 0:
            raise TypeError("Criteria is not valid!")
        searchCriteria ='AND'.join([f' {item[0]} LIKE ? ' for item in criteria.items()])

        prepared = tuple()
        for k, v in criteria.items():
            if k not in self.allowedColumns:
                raise TypeError("Not a valid Column!")

            prepared = prepared + (
                (self.cipher.encrypt(v) if k in self.encryptColumns else v),
            )


        result = (self.connection.execute(f"SELECT * FROM {table} WHERE {searchCriteria}", prepared).fetchall())
        return result

