import re

from toolbox.actions.action import Action
from translator.translate import Translator


class CensorAction(Action):
    name = "CensorAction"
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
            if clean_censored_phrase := censored_phrase.strip():
                pattern = self._compile_pattern(clean_censored_phrase)
                text = pattern.sub("[censored]", text)
        return text

    @classmethod
    def to_dict(cls, language: str = "pl_PL") -> dict:
        t = Translator(language)
        return {
            "usage": "text",
            "name": cls.__name__,
            "label": "censor_label",
            "title": t.translate("censor_title"),
            "description": t.translate("censor_description"),
            "args": {
                "censored_phrases": {
                    "type": "list[str]",
                    "legend": t.translate("censored_phrases_legend"),
                },
                "is_case_sensitive": {
                    "type": "bool",
                    "legend": t.translate("is_case_sensitive_legend"),
                },
            },
        }

    def _compile_pattern(self, censored_phrase: str) -> re.Pattern:
        if self.is_case_sensitive:
            return re.compile(re.escape(censored_phrase))
        return re.compile(re.escape(censored_phrase), flags=re.IGNORECASE)
