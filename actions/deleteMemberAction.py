from typing import Any, Dict, List
from responses.memberResponse import MemberResponse

from interface.IResponses import IResponse
from interface.IActions import IActions

from services.memberService import MemberService
from services.sessionService import SessionService

class DeleteMemberAction(IActions):
    session: SessionService
    memberS: MemberService

    def __init__(self, session: SessionService, memberS: MemberService) -> None:
        self.session = session
        self.memberS = memberS

    def is_actived(self) -> bool:
        return (
            self.session.loginCheck() and self.session.currentUser.role in ['system_administrator', 'super_admin']
        )

    def arguments(self) -> List[IResponse]:
        return [MemberResponse(self.memberS)]

    def handle(self, arguments: Dict[str, Any]) -> None:
        self.memberS.delete(arguments['member'].id)
        print('Member deleted!')
