from typing import Any, Dict, List
from model import user
from interface import IDatabaseActions
from helpers.passwordHasher import PasswordHasher


class UserService():

    DatabaseAction: IDatabaseActions[user]
    pwHasher: PasswordHasher



    def __int__(self, databaseActions: IDatabaseActions[user], ):
        pass