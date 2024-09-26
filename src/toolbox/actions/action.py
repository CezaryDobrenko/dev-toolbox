from abc import ABC, abstractmethod


class Action(ABC):
    name: str

    @abstractmethod
    def execute(self, text: str) -> str:
        pass

    @classmethod
    @abstractmethod
    def to_dict(cls, language: str) -> dict:
        pass
