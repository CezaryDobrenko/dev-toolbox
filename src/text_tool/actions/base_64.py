import base64

from toolbox.actions.action import Action


class FromBase64Action(Action):
    name = "FromBase64"

    def execute(self, text: str) -> str:
        return base64.b64decode(text).decode()

    @classmethod
    def to_dict(cls) -> dict:
        return {
            "name": cls.__name__,
            "label": "from_base64_label",
            "usage": "text",
            "args": {},
        }


class ToBase64Action(Action):
    name = "ToBase64"

    def execute(self, text: str) -> str:
        text_bytes = text.encode("utf-8")
        return base64.b64encode(text_bytes).decode()

    @classmethod
    def to_dict(cls) -> dict:
        return {
            "name": cls.__name__,
            "label": "to_base64_label",
            "usage": "text",
            "args": {},
        }
