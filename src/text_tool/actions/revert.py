from toolbox.actions.action import Action


class RevertAction(Action):
    name = "Revert"

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
