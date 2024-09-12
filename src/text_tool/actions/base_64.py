import base64

from action import Action


class FromBase64(Action):
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


class ToBase64(Action):
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
