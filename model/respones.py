from abc import abstractmethod
from typing import List, Union

from responses.emptyResponse import EmptyResponse
from interface.IResponses import IResponse
from interface.IModel import IModel

class ResponseModel(IResponse[IModel]):
    model: List[IModel]
    def __init__(self, name:str, prompt:str, model: List[IModel]) -> None:
        super().__init__(name, prompt)
        self.model = model

    @abstractmethod
    def print(self, model: List[IModel]) -> None:
        pass

    def ask(self) -> IModel:
        self.print(self.model)
        select = None
        while True:
            select = EmptyResponse('id', self._prompt).ask()
            validate = self.validate(select)
            if validate is True: break
            if isinstance(validate, str): print(validate)
            if validate is False: print(f'Invalid {self.get_name()}')
        return  self.sanitize(select)

    def validate(self, value: str) -> Union[str, bool]:
        return len(list(filter(lambda model: str(model.get_id()) == value, self.model))) > 0

    def sanitize(self, value: str) -> IModel:
        return list(filter(lambda model: str(model.get_id()) == value, self.model))[0]

