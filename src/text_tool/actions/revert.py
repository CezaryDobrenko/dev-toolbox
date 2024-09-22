from toolbox.actions.action import Action


class RevertAction(Action):
    name = "RevertAction"

    def execute(self, text: str) -> str:
        return text[::-1]

    @classmethod
    def to_dict(cls) -> dict:
        return {
            "usage": "text",
            "name": cls.__name__,
            "label": "revert_label",
            "title": "revert_title",
            "description": "revert_description",
            "args": {},
        }
