from typing import Any, Dict, List
from interface.IResponses import IResponse
from interface.IActions import IActions
from helpers.initializer import ShowMember
from services.sessionService import SessionService
from services.memberService import MemberService

class ViewMemberAction(IActions):

    memberS: MemberService
    session: SessionService

    def __init__(self, session: SessionService, memberS: MemberService) -> None:
        self.session = session
        self.memberS = memberS

    def is_actived(self) -> bool:
        return self.session.loginCheck()
    def arguments(self) -> List[IResponse]:
        return []
    def handle(self, arguments: Dict[str, Any]) -> None:
        ShowMember(self.memberS.showAllMembers())