import json

from django.http import HttpResponse
from django.views.generic import TemplateView

from text_tool.actions import TEXT_ACTIONS_LIST
from text_tool.service.action_runner import TextActionRunner
from translator.translate import Translator


class DashboardView(TemplateView):
    template_name = "toolbox/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        language = kwargs.get("lang", "pl_PL")
        return (
            context
            | self.setup_custom_context_data(language)
            | self.setup_action_schema(language)
        )

    def post(self, request, **kwargs):
        data = request.POST
        text = data["text"]
        actions = json.loads(data["actions"])
        return HttpResponse(json.dumps({"result": TextActionRunner(actions).run(text)}))

    def setup_action_schema(self, language: str) -> dict:
        schema = {}
        for action in TEXT_ACTIONS_LIST:
            action_data = action.to_dict(language)
            schema[action_data["label"]] = action_data
        return {"actions": schema}

    def setup_custom_context_data(self, language: str) -> dict:
        t = Translator(language)
        static_labels = [
            "delete_label",
            "select_action_label",
            "execute_actions_label",
            "create_new_element_label",
            "base_text_placeholder_label",
            "result_text_placeholder_label",
        ]
        return {label: t.translate(label) for label in static_labels}
