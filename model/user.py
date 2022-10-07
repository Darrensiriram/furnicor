from dataclasses import dataclass,field
from datetime import datetime
from typing import Optional

from interface.IModel import IModel


def currentTime() -> datetime:
    return datetime.now()

@dataclass
class User(IModel):
    username: str
    role: str
    password: str = field(repr=False)
    salt: str = field(repr=False)
    id: Optional[int] = None
    created_at: datetime = field(default_factory=currentTime)
    has_temp_password: bool = field(default=False)

    def userInfo(self) -> str:
        return f'{self.id}, {self.username}'

    def getId(self) -> int:
        return self.id
