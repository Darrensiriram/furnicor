from typing import Dict, Optional
from responses.selectResponse import SelectResponse

class SelectCityResponse(SelectResponse[str]):
    def __init__(self, name:str, prompt:str, choices:Optional[Dict[str,str]] = None) -> None:
        if choices is None:
            choices = {
                'rotterdam': 'Rotterdam',
                'den_haag': 'Den Haag',
                'amstedam': 'Amsterdam',
                'utrecht': 'Utrecht'
            }
        super().__init__(name, prompt, choices)