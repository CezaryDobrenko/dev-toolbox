from abc import ABC, abstractmethod

from toolbox.actions.action import Action


class Parser(ABC):
    @staticmethod
    @abstractmethod
    def parse_actions(raw_actions: dict) -> list[Action, dict]:
        pass
