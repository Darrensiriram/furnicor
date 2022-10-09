from typing import Any, Dict, List
from responses.emailResponse import EmailResponse
from responses.phoneResponse import PhoneResponse
from responses.postalCodeResponse import PostalCodeResponse
from responses.selectCityRepsonse import SelectCityResponse
from responses.emptyResponse import EmptyResponse
from interface.IActions import IActions
from interface.IResponses import IResponse
from services.sessionService import SessionService
from services.memberService import MemberService


class CreateMemberAction(IActions):
    session: SessionService
    memberS: MemberService

    def __init__(self, session: SessionService, memberS: MemberService) -> None:
        self.session = session
        self.memberS = memberS

    def is_actived(self) -> bool:
        return  self.session.loginCheck()

    def arguments(self) -> List[IResponse]:
        return [
            EmptyResponse('first_name', 'First name: '),
            EmptyResponse('last_name', 'Last name: '),
            EmptyResponse('street_name', 'Street name: '),
            EmptyResponse('house_number', 'House number: '),
            PostalCodeResponse(),
            SelectCityResponse(),
            EmailResponse(),
            PhoneResponse(),
        ]
    def handle(self, arguments: Dict[str, Any]) -> None:
        m = self.memberS.createMember(
            arguments['first_name'],
            arguments['last_name'],
            arguments['street_name'],
            arguments['house_number'],
            arguments['postalCode'],
            arguments['city'],
            arguments['email'],
            arguments['phone'],
        )
        print(f"Member created! welcome: {m.first_name}")