from toolbox.actions.action import Action

from .base_64 import FromBase64Action, ToBase64Action
from .censor import CensorAction
from .replace import ReplaceAction
from .revert import RevertAction

TEXT_ACTIONS_LIST: list[Action] = [
    ToBase64Action,
    FromBase64Action,
    CensorAction,
    ReplaceAction,
    RevertAction,
]

TEXT_ACTIONS_DICT: dict[str, Action] = {
    ToBase64Action.name: ToBase64Action,
    FromBase64Action.name: FromBase64Action,
    CensorAction.name: CensorAction,
    ReplaceAction.name: ReplaceAction,
    RevertAction.name: RevertAction,
}
