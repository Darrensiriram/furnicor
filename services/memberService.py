from typing import Any, Dict, List

from model.member import Member
from interface.IDatabaseActions import IDatabaseActions
from services.logService import LogService

class MemberService():
    action: IDatabaseActions[Member]
    log: LogService

    def __init__(self, action: IDatabaseActions[Member], log: LogService) -> None:
        self.action = action
        self.log = log


    def createMember(self, first_name:str, last_name: str, street_name: str, house_number: str, postalCode: str, city: str, email:str, phone:str)-> Member:
        member = Member(
            first_name,
            last_name,
            street_name,
            house_number,
            postalCode,
            city,
            email,
            phone
        )

        self.action.create(member)
        self.log.logInfo(f'Member created')
        return member

    def showAllMembers(self) -> List[Member]:
        result = self.action.selectAll()
        self.log.logInfo(f'Showed all members with a total of {len(result)}')
        return result

    def updateMember(self, id:int, updates: Dict[str, Any]) -> Member:
        updateQuery = self.action.update(id, updates)
        self.log.logInfo(f"Member has been updated! with ID: {id}")
        return updateQuery

    def delete(self, id:int) -> None:
        result = self.action.selectOne(id)
        self.log.logInfo(f'Member has been deleted! {result}')
        self.action.delete(id)

    def searchMember(self, criteria:str) -> List[Member]:
        criteria.lower()
        searchResults = []
        member = self.action.selectAll()

        for m in member:
            if criteria in str(m.id).lower():
                searchResults.append(m)
            elif criteria in m.first_name.lower():
                searchResults.append(m)
            elif criteria in m.last_name.lower():
                searchResults.append(m)
            elif criteria in m.city.lower():
                searchResults.append(m)
            elif criteria in m.phone.lower():
                searchResults.append(m)
            elif criteria in m.email.lower():
                searchResults.append(m)
            elif criteria in m.street_name.lower():
                searchResults.append(m)
            elif criteria in m.postalCode.lower():
                searchResults.append(m)
            elif criteria in m.house_number.lower():
                searchResults.append(m)

        self.log.logInfo(f"Found a total of {len(searchResults)}, with the use of this criteria: {criteria}")
        return searchResults

