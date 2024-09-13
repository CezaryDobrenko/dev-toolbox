import re

from toolbox.actions.action import Action


class CensorAction(Action):
    name = "Censor"
    censored_phrases: list[str]
    is_case_sensitive: bool

    def __init__(
        self,
        censored_phrases: list[str],
        is_case_sensitive: bool = True,
    ):
        censored_phrases.sort(key=len)
        self.censored_phrases = censored_phrases
        self.is_case_sensitive = is_case_sensitive

    def execute(self, text: str) -> str:
        for censored_phrase in self.censored_phrases:
            pattern = self._compile_pattern(censored_phrase)
            text = pattern.sub("[censored]", text)
        return text

    @classmethod
    def to_dict(cls) -> dict:
        return {
            "name": cls.__name__,
            "label": "censor_label",
            "usage": "text",
            "args": {"censored_phrases": "list[str]", "is_case_sensitive": "bool"},
        }

    def _compile_pattern(self, censored_phrase: str) -> re.Pattern:
        if self.is_case_sensitive:
            return re.compile(re.escape(censored_phrase))
        return re.compile(re.escape(censored_phrase), flags=re.IGNORECASE)
