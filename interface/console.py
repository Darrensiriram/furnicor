import os
from typing import Any,Dict
from interface.icommand import ICommand

class Console:

    title = None
    width = None
    __commands: Dict[str, ICommand]
    def __init__(self, title, width: int = os.get_terminal_size().columns) -> None:
        self.title = title
        self.width = width

    def createCommands(self, description: str , command: ICommand):
        self.__commands[description] = command

    def startApplication(self) -> None:
        while True:
            self.__print_title()
            command = self.showCommands()
            print()
            command.handle(self.__get_arguments_for_command(command))
            print()
            input("Press Space to back to the command list.")

            for _ in range(10):
                print()


    def __print_title(self):
        print()
        print(f'{self.title}')
        print()


    def showCommands(self):
        enable_cmd = list(filter(lambda entry: entry[1].is_enabled(), self.__commands.items()))

        i = 1

        for(name, _) in enable_cmd:
            print(f'{i} - {name}')
            i += 1
        print()
        choise = None


        while True:
            try:
                choise = int(input('Chose a number: '))
            except ValueError:
                print('Incorrect choice!')
                continue

            if choise < 1 or choise > len(enable_cmd):
                print("Index out of range!")
                continue
            break
        return enable_cmd[choise - 1][1]

    def __get_arguments_for_command(cls,command: ICommand) -> Dict[str, Any]:
        arguments = {}
        for argument in command.arguments():
            arguments[argument.get_name()] = argument.ask()
        return arguments


