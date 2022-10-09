
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Set

from interface.IModel import IModel
from model.user import User

@dataclass
class Log(IModel):

    message: str
    user: Optional[User] = field(default=None)
    id: Optional[int] = field(default=None)
    is_suspicious: bool = field(default=False)
    created_at: datetime = field(default_factory=datetime.now)


    def getId(self) -> int:
        return self.id or -1
