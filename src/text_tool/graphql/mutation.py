import graphene

from text_tool.service.action_service import (
    run_multiple_text_actions,
    run_revert_text_action,
)


class RunTextRevertAction(graphene.Mutation):
    class Arguments:
        base_text = graphene.String(required=True)

    result = graphene.String()

    def mutate(self, info: graphene.ResolveInfo, base_text: str) -> str:
        result = run_revert_text_action(base_text=base_text)
        return RunTextRevertAction(result=result)


class RunTextMultipleActions(graphene.Mutation):
    class Arguments:
        base_text = graphene.String(required=True)
        actions = graphene.JSONString(required=True)

    result = graphene.String()

    def mutate(self, info: graphene.ResolveInfo, base_text: str, actions: dict) -> str:
        result = run_multiple_text_actions(base_text=base_text, actions=actions)
        return RunTextRevertAction(result=result)


class TextActionMutation(graphene.ObjectType):
    run_text_revert_action = RunTextRevertAction.Field()
    run_text_multiple_actions = RunTextMultipleActions.Field()
