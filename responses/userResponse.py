from typing import List
from helpers.initializer import ShowUsers
from interface.IModel import IModel
from services.userService import UserService
from model.respones import ResponseModel


class UserResponse(ResponseModel):
    def __init__(self, userS: UserService, access: False, name:str = 'user', prompt:str = 'Select user: ' ) -> None:
        users = userS.showAllUsers() if access else userS.showAllEditableUsers()
        super().__init__(name, prompt, users)

    def print(self, model: List[IModel]) -> None:
        ShowUsers(model)