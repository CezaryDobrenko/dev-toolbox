import base64

from toolbox.actions.action import Action


class FromBase64Action(Action):
    name = "FromBase64Action"

    def execute(self, text: str) -> str:
        return base64.b64decode(text).decode(errors="ignore")

    @classmethod
    def to_dict(cls) -> dict:
        return {
            "usage": "text",
            "name": cls.__name__,
            "label": "from_base64_label",
            "title": "from_base64_title",
            "description": "from_base64_description",
            "args": {},
        }


class ToBase64Action(Action):
    name = "ToBase64Action"

    def execute(self, text: str) -> str:
        text_bytes = text.encode("utf-8")
        return base64.b64encode(text_bytes).decode()

    @classmethod
    def to_dict(cls) -> dict:
        return {
            "usage": "text",
            "name": cls.__name__,
            "label": "to_base64_label",
            "title": "to_base64_title",
            "description": "to_base64_description",
            "args": {},
        }
