from toolbox.actions.action import Action


class ReplaceAction(Action):
    name = "Replace"
    old_text: str
    new_text: str

    def __init__(self, old_text: str, new_text: str):
        self.old_text = old_text
        self.new_text = new_text

    def execute(self, text: str) -> str:
        return text.replace(self.old_text, self.new_text)

    @classmethod
    def to_dict(cls) -> dict:
        return {
            "name": cls.__name__,
            "label": "replace_label",
            "description": "replace_description",
            "usage": "text",
            "args": {
                "old": {"type": "str", "label": "old_label"},
                "new": {"type": "str", "label": "new_label"},
            },
        }
