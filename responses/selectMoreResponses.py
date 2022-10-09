from typing import Dict, List, Union
from responses.selectResponse import SelectResponse
from interface.IResponses import IResponse

class SelectMoreResponses(IResponse[List[str]]):
    choices: Dict[str,str]

    def __init__(self, name:str, prompt:str, destroy:str, choices: Dict[str,str]):
        super().__init__(name,prompt)

        choices['abort'] = destroy
        self.choices = choices

    def ask(self) -> List[str]:
        response = SelectResponse(self._name, self._prompt, self.choices)
        result = []
        while True:
            column = response.ask()
            if column == 'abort' and len(result) == 0:
                print('Select a value please')
                continue
            if column == 'abort':
                break
            print(f'Added, type {len(self.choices)} to stop selecting')
            result.append(column)

        return result

    def _validate(self, value: str) -> Union[str, bool]:
        return True
    def _sanitize(self, value: str) -> List[str]:
        return [value]

