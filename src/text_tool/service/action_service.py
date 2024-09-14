from text_tool.actions.base_64 import FromBase64Action, ToBase64Action
from text_tool.actions.censor import CensorAction
from text_tool.actions.replace import ReplaceAction
from text_tool.actions.revert import RevertAction
from text_tool.service.action_runner import TextActionRunner


def run_to_base64_text_action(base_text: str) -> str:
    action = ToBase64Action()
    return action.execute(base_text)


def run_from_base64_text_action(base_text: str) -> str:
    action = FromBase64Action()
    return action.execute(base_text)


def run_replace_text_action(base_text: str, old_text: str, new_text: str) -> str:
    action = ReplaceAction(old_text, new_text)
    return action.execute(base_text)


def run_censor_text_action(
    base_text: str, censored_phrases: list[str], is_case_sensitive: bool = True
) -> str:
    action = CensorAction(censored_phrases, is_case_sensitive)
    return action.execute(base_text)


def run_revert_text_action(base_text: str) -> str:
    action = RevertAction()
    return action.execute(base_text)


def run_multiple_text_actions(base_text: str, actions: dict) -> str:
    runner = TextActionRunner(actions)
    return runner.run(base_text)
