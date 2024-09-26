from toolbox.actions.action import Action
from translator.translate import Translator


class RevertAction(Action):
    name = "RevertAction"

    def execute(self, text: str) -> str:
        return text[::-1]

    @classmethod
    def to_dict(cls, language: str = "pl_PL") -> dict:
        t = Translator(language)
        return {
            "usage": "text",
            "name": cls.__name__,
            "label": "revert_label",
            "title": t.translate("revert_title"),
            "description": t.translate("revert_description"),
            "args": {},
        }
