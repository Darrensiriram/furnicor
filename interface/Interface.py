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
            action.handle(self.__get_arguments_for_Actions(action))
            print()
            input("Press Enter to back to the command list.")

            for _ in range(2):
                print()


    def print_title(self):
        print()
        print(f'{self.title}')
        print()


    def showActions(self):
        activateCommands = list(filter(lambda entry: entry[1].is_actived() ,self.Actions.items()))

        i = 1

        for(name, _) in activateCommands:
            print(f'{i} - {name}')
            i += 1
        print()
        choice = None

        while True:
            try:
                choice = int(input('Choose a number: '))
            except ValueError:
                print('Incorrect choice!')
                continue

            if choice < 1 or choice > len(activateCommands):
                print("Index out of range!")
                continue
            break
        return activateCommands[choice - 1][1]

    def __get_arguments_for_Actions(cls, action: IActions) -> Dict[str, Any]:
        arguments = {}
        for argument in action.arguments():
            arguments[argument.get_name()] = argument.ask()
        return arguments


