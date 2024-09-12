from action import Action


class Revert(Action):
    def execute(self, text: str) -> str:
        return text[::-1]

    @classmethod
    def to_dict(cls) -> dict:
        return {
            "name": cls.__name__,
            "label": "revert_label",
            "usage": "text",
            "args": {},
        }
