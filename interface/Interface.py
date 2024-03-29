import os
from typing import Any,Dict
from interface.IActions import IActions
class Interface:
    """Interface of the application"""

    title: str
    Actions: Dict[str, IActions] = {}
    def __init__(self, title) -> None:
        self.title = title

    def createActions(self, description: str, action: IActions) -> None:
        self.Actions[description] = action

    def startApplication(self) -> None:
        while True:
            self.print_title()
            action = self.showActions()
            print()
            action.handle(self.__get_arguments_for_Actions())
            print()
            input("Press Space to back to the command list.")

            for _ in range(10):
                print()


    def print_title(self):
        print()
        print(f'{self.title}')
        print()


    def showActions(self):
        activateCommands = list(filter(lambda entry: entry[1].is_actived(),self.Actions.items()))

        i = 1

        for(name, _) in activateCommands:
            print(f'{i} - {name}')
            i += 1
        print()
        choise = None

        while True:
            try:
                choise = int(input('Choose a number: '))
            except ValueError:
                print('Incorrect choice!')
                continue

            if choise < 1 or choise > len(activateCommands):
                print("Index out of range!")
                continue
            break
        return activateCommands[choise - 1][1]

    def __get_arguments_for_Actions(cls, action: IActions) -> Dict[str, Any]:
        arguments = {}
        for argument in action.arguments():
            arguments[argument.get_name()] = argument.ask()
        return arguments


