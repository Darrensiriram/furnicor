from dataclasses import dataclass, field
from datetime import datetime
from random import randint

from interface.IModel import IModel

def createId() -> int:
    randomDigits = str(randint(1,9) + randint(1,9))
    totalDigit = sum(int(digit) for digit in randomDigits)
    modulo = str(totalDigit % 10)

    return int(randomDigits + modulo)


def currentTime() -> datetime:
    return datetime.now()

class Member(IModel):
    first_name: str
    last_name: str
    street_name: str
    house_number: str
    postalCode: str
    city:  str
    email: str
    phone: str
    id: int = field(default_factory=createId)
    created_at: datetime = field(default_factory=currentTime)

    def getId(self) -> int:
        return self.id
    def memberInfo(self) -> str:
        return f'{self.first_name} {self.last_name}. {self.id}'
