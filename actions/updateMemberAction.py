from typing import Any, Dict, List
from responses.emailResponse import EmailResponse
from responses.memberResponse import MemberResponse
from responses.phoneResponse import PhoneResponse
from responses.selectCityRepsonse import SelectCityResponse
from responses.emptyResponse import EmptyResponse
from responses.selectMoreResponses import SelectMoreResponses
from responses.postalCodeResponse import PostalCodeResponse
from interface.IActions import  IActions
from interface.IResponses import IResponse
from services.memberService import MemberService
from services.sessionService import SessionService
from helpers.initializer import ShowMember

class UpdateMemberAction(IActions):
    session: SessionService
    memberS: MemberService

    def __init__(self, session: SessionService, memberS: MemberService) -> None:
        self.session = session
        self.memberS = memberS

    def is_actived(self) -> bool:
        return self.session.loginCheck()

    def arguments(self) -> List[IResponse]:
        return [
            MemberResponse(self.memberS),
            SelectMoreResponses(
                'updateCol',
                'Select the column to update: ',
                'updating the password.... ',
                {
                    'first_name': 'First name',
                    'last_name': 'Last name',
                    'street_name': 'Street name',
                    'house_number': 'House number',
                    'city': 'City',
                    'postalCode': 'Postal Code',
                    'email': 'Email',
                    'phone': 'Phone',
                }
            ),
        ]

    def handle(self, arguments: Dict[str, Any]) -> None:
        columnUpdate = arguments['updateCol']
        member = arguments['member']

        updates = {}
        if 'first_name' in columnUpdate:
            updates['first_name'] = EmptyResponse('first_name', 'First name: ').ask()
        if 'last_name' in columnUpdate:
            updates['last_name'] = EmptyResponse('last_name', 'Last name: ').ask()
        if 'street_name' in columnUpdate:
            updates['street_name'] = EmptyResponse('street_name', 'Street name: ').ask()
        if 'house_number' in columnUpdate:
            updates['house_number'] = EmptyResponse('house_number', 'House number: ').ask()
        if 'city' in columnUpdate:
            updates['city'] = SelectCityResponse().ask()
        if 'postalCode' in columnUpdate:
            updates['postalCode'] = PostalCodeResponse().ask()
        if 'email' in columnUpdate:
            updates['email'] = EmailResponse().ask()
        if 'phone' in columnUpdate:
            updates['phone'] = PhoneResponse().ask()

        updated = self.memberS.updateMember(member.id, updates)

        print('Member has been updated: ')
        ShowMember([updated])
