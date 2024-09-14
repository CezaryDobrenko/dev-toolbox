import graphene

from text_tool.service.action_service import (
    run_censor_text_action,
    run_from_base64_text_action,
    run_multiple_text_actions,
    run_replace_text_action,
    run_revert_text_action,
    run_to_base64_text_action,
)


class RunTextRevertAction(graphene.Mutation):
    class Arguments:
        base_text = graphene.String(required=True)

    result = graphene.String()

    def mutate(self, info: graphene.ResolveInfo, base_text: str) -> str:
        result = run_revert_text_action(base_text=base_text)
        return RunTextRevertAction(result=result)


class RunTextToBase64Action(graphene.Mutation):
    class Arguments:
        base_text = graphene.String(required=True)

    result = graphene.String()

    def mutate(self, info: graphene.ResolveInfo, base_text: str) -> str:
        result = run_to_base64_text_action(base_text=base_text)
        return RunTextToBase64Action(result=result)


class RunTextFromBase64Action(graphene.Mutation):
    class Arguments:
        base_text = graphene.String(required=True)

    result = graphene.String()

    def mutate(self, info: graphene.ResolveInfo, base_text: str) -> str:
        result = run_from_base64_text_action(base_text=base_text)
        return RunTextFromBase64Action(result=result)


class RunTextReplaceAction(graphene.Mutation):
    class Arguments:
        base_text = graphene.String(required=True)
        old_text = graphene.String(required=True)
        new_text = graphene.String(required=True)

    result = graphene.String()

    def mutate(
        self, info: graphene.ResolveInfo, base_text: str, old_text: str, new_text: str
    ) -> str:
        result = run_replace_text_action(base_text, old_text, new_text)
        return RunTextReplaceAction(result=result)


class RunTextCensorAction(graphene.Mutation):
    class Arguments:
        base_text = graphene.String(required=True)
        censored_phrases = graphene.List(graphene.String, required=True)
        is_case_sensitive = graphene.Boolean(required=True)

    result = graphene.String()

    def mutate(
        self,
        info: graphene.ResolveInfo,
        base_text: str,
        censored_phrases: list[str],
        is_case_sensitive: bool,
    ) -> str:
        result = run_censor_text_action(base_text, censored_phrases, is_case_sensitive)
        return RunTextCensorAction(result=result)


class RunTextMultipleActions(graphene.Mutation):
    class Arguments:
        base_text = graphene.String(required=True)
        actions = graphene.JSONString(required=True)

    result = graphene.String()

    def mutate(self, info: graphene.ResolveInfo, base_text: str, actions: dict) -> str:
        result = run_multiple_text_actions(base_text=base_text, actions=actions)
        return RunTextMultipleActions(result=result)


class TextActionMutation(graphene.ObjectType):
    run_text_revert_action = RunTextRevertAction.Field()
    run_text_to_base64_action = RunTextToBase64Action.Field()
    run_text_from_base64_action = RunTextFromBase64Action.Field()
    run_text_replace_action = RunTextReplaceAction.Field()
    run_text_censor_action = RunTextCensorAction.Field()
    run_text_multiple_actions = RunTextMultipleActions.Field()
