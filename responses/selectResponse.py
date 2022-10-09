from typing import Dict, Union
from interface.IResponses import CorrectType, IResponse


class SelectResponse(IResponse[CorrectType]):
    choices = Dict[CorrectType, str]

    def __init__(self, name: str, prompt: str, choices: Dict[CorrectType, str]):
        super().__init__(name, prompt)
        self.choices = choices

    def ask(self) -> CorrectType:
        i = 1
        for choiceName in self.choices.values():
            print(f'{i} -> {choiceName}')
            i += 1
        print()

        choice = None
        while True:
            try:
                choice = int(input(self._prompt))
            except ValueError:
                print("Oops!, that is probably not a number. ")
                continue

            if choice < 1 or choice > len(self.choices):
                print('Hello sir!, that is not a valid choice!')
                continue

            choice = list(self.choices.values())[choice - 1]
            validate = self._validate(choice)

            if isinstance(validate, str):
                print(validate)
                continue

            if validate is False:
                print(f'Invalid choice for the reponse {self.get_name()}, do it again')
                continue
            break
        return self._sanitize(choice)

    def _validate(self, value: str) -> Union[str, bool]:
        return True

    def _sanitize(self, value: str) -> CorrectType:
        return self.valueTokey(value)

    def valueTokey(self, value: str) -> CorrectType:
        return [choice for (choice, value) in self.choices.items() if value == value][0]
