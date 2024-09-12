from action import Action

from .base_64 import FromBase64, ToBase64
from .censor import Censor
from .replace import Replace
from .revert import Revert

TEXT_ACTIONS: list[Action] = [
    ToBase64,
    FromBase64,
    Censor,
    Replace,
    Revert,
]
