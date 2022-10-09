from typing import List
from helpers.initializer import ShowMember
from interface.IModel import IModel
from services.memberService import MemberService
from model.respones import ResponseModel

class MemberResponse(ResponseModel):
    def __init__(self, memberS: MemberService, name:str = 'member', prompt:str = 'choose member from the list') ->None:
        super().__init__(name, prompt, memberS.showAllMembers())


    def print(self, model: List[IModel]) -> None:
        ShowMember(model)
