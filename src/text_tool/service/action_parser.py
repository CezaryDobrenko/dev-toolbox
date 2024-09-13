from text_tool.actions import TEXT_ACTIONS_DICT
from toolbox.actions.parser import Parser


class TextActionParser(Parser):
    @staticmethod
    def parse_actions(raw_actions: dict):
        selected_actions = []
        for action_name, arguments in raw_actions.items():
            if action_name not in TEXT_ACTIONS_DICT.keys():
                raise Exception(f"found_unrecognised_action: {action_name}")
            selected_actions.append([TEXT_ACTIONS_DICT[action_name], arguments])
        return selected_actions
