from abc import ABC, abstractmethod

from toolbox.actions.action import Action
from toolbox.actions.parser import Parser


class Runner(ABC):
    avalible_type: str
    selected_actions: list[Action, dict]
    parser: Parser

    @abstractmethod
    def run(self, base_text: str) -> str:
        pass
