from action import Action


class Replace(Action):
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
            "usage": "text",
            "args": {"old": "str", "new": "str"},
        }
