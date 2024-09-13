import graphene

from text_tool.actions import TEXT_ACTIONS_LIST
from toolbox.graphql.schema.action_schema import ActionSchemaNode


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="GraphQL ready!")
    actions_schema = graphene.List(ActionSchemaNode)

    def resolve_actions_schema(self, info: graphene.ResolveInfo, **kwargs):
        return [ActionSchemaNode.from_action(action) for action in TEXT_ACTIONS_LIST]
