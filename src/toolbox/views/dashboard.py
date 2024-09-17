from django.views.generic import TemplateView
from text_tool.actions import TEXT_ACTIONS_LIST


class DashboardView(TemplateView):
    template_name = "toolbox/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        schema = {}
        for action in TEXT_ACTIONS_LIST:
            action_data = action.to_dict()
            schema[action_data["label"]] = action_data
        context["actions"] = schema
        return context
