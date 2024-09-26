import json

from toolbox.settings import BASE_TRANSLATION_DIR

SUPPORTED_LANGUAGES = [
    "pl_PL",
    "en_EN",
]


class Translator:
    translation_data: dict

    def __init__(self, language: str):
        if language not in SUPPORTED_LANGUAGES:
            raise Exception("unsupported_language")

        self.translation_data = self._load_translation_data(language)

    def translate(self, text: str) -> str:
        return self.translation_data.get(text, "translation_not_found")

    def _load_translation_data(self, language: str) -> dict:
        with open(f"{BASE_TRANSLATION_DIR}/{language}.json", "r") as file:
            translation_data = json.load(file)
        return translation_data
