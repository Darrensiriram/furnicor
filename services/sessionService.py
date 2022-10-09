from typing import Optional
from model.user import User


class SessionService():
    __user: Optional[User] = None

    @property
    def currentUser(self) -> User:
        if self.__user is None:
            raise Exception(("There is no user available"))
        return self.__user

    @currentUser.setter
    def currentUser(self, user: Optional[User]):
        self.__user = user

    def loginCheck(self) -> bool:
        return self.__user is not None

    def closeSession(self) -> None:
        self.__user = None
