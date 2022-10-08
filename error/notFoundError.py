from typing import Optional
class NotFound(Exception):
    descirption: str

    def __init__(self, description:str, message: Optional[str] = None) -> None:
        self.descirption = description

        if message is None:
            message = f'{description} not found.'

        super().__init__(message)