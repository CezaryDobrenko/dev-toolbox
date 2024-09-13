from text_tool.service.action_parser import TextActionParser
from toolbox.actions.action import Action
from toolbox.actions.runner import Runner


class TextActionRunner(Runner):
    avalible_type = "text"
    parser = TextActionParser
    selected_actions: list[Action, dict]

    def __init__(self, raw_actions: dict):
        self.selected_actions = self.parser.parse_actions(raw_actions)

    def run(self, base_text: str) -> str:
        for _action, _arguments in self.selected_actions:
            action: Action = _action(**_arguments)
            base_text = action.execute(base_text)
        return base_text
