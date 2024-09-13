from text_tool.actions.revert import RevertAction
from text_tool.service.action_runner import TextActionRunner


def run_revert_text_action(base_text: str) -> str:
    return RevertAction().execute(base_text)


def run_multiple_text_actions(base_text: str, actions: dict) -> str:
    runner = TextActionRunner(actions)
    return runner.run(base_text)
