from typing import Optional
from model.user import User

class SessionService():
    user = Optional[User] = None

    @property
    def currentUser(self) -> User:
        if self.user is None:
            raise Exception(("There is no user available"))
        return self.user

    @currentUser.setter
    def currentUser(self, user: Optional[User]):
        self.user = user

    def loginCheck(self) -> bool:
        return self.user is not None

    def closeSession(self)-> None:
        self.user = None



