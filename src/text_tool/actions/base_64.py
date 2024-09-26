import base64

from toolbox.actions.action import Action
from translator.translate import Translator


class FromBase64Action(Action):
    name = "FromBase64Action"

    def execute(self, text: str) -> str:
        return base64.b64decode(text).decode(errors="ignore")

    @classmethod
    def to_dict(cls, language: str = "pl_PL") -> dict:
        t = Translator(language)
        return {
            "usage": "text",
            "name": cls.__name__,
            "label": "from_base64_label",
            "title": t.translate("from_base64_title"),
            "description": t.translate("from_base64_description"),
            "args": {},
        }


class ToBase64Action(Action):
    name = "ToBase64Action"

    def execute(self, text: str) -> str:
        text_bytes = text.encode("utf-8")
        return base64.b64encode(text_bytes).decode()

    @classmethod
    def to_dict(cls, language: str = "pl_PL") -> dict:
        t = Translator(language)
        return {
            "usage": "text",
            "name": cls.__name__,
            "label": "to_base64_label",
            "title": t.translate("to_base64_title"),
            "description": t.translate("to_base64_description"),
            "args": {},
        }
