from typing import Any, Dict, List
from interface.IResponses import IResponse
from interface.IActions import IActions
from helpers.initializer import ShowMember
from services.sessionService import SessionService
from services.memberService import MemberService
from responses.emptyResponse import EmptyResponse


class SearchMemberAction(IActions):
    session: SessionService
    memberS: MemberService

    def __init__(self, session: SessionService, memberS: MemberService) -> None:
        self.session = session
        self.memberS = memberS

    def is_actived(self) -> bool:
        return self.session.loginCheck()

    def arguments(self) -> List[IResponse]:
        return [
            EmptyResponse('criteria', 'Search criteria: ')
        ]

    def handle(self, arguments: Dict[str, Any]) -> None:
        member = self.memberS.searchMember(arguments['criteria'])
        ShowMember(member)