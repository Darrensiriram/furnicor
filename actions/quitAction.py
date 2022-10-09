import sys
from typing import Any, Dict, List

from interface.IActions import IActions
from interface.IResponses import IResponse

class QuitAction(IActions):
    def is_actived(self) -> bool:
        return True
    def arguments(self) -> List[IResponse]:
        return []
    def handle(self, arguments: Dict[str, Any]) -> None:
        sys.exit()