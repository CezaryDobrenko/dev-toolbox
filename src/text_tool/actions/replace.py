from toolbox.actions.action import Action
from translator.translate import Translator


class ReplaceAction(Action):
    name = "ReplaceAction"
    old_text: str
    new_text: str
    ignore_error: bool

    def __init__(self, old_text: str, new_text: str, ignore_error: bool):
        self.old_text = old_text
        self.new_text = new_text
        self.ignore_error = ignore_error

    def execute(self, text: str) -> str:
        return text.replace(self.old_text, self.new_text)

    @classmethod
    def to_dict(cls, language: str = "pl_PL") -> dict:
        t = Translator(language)
        return {
            "usage": "text",
            "name": cls.__name__,
            "label": "replace_label",
            "title": t.translate("replace_title"),
            "description": t.translate("replace_description"),
            "args": {
                "old_text": {"type": "str", "legend": t.translate("old_legend")},
                "new_text": {"type": "str", "legend": t.translate("new_legend")},
                "ignore_error": {"type": "bool", "legend": t.translate("error_legend")},
            },
        }
