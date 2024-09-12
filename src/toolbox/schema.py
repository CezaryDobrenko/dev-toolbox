from __future__ import annotations

import graphene
from action import Action
from text_tool.actions import TEXT_ACTIONS


class ActionArgumentNode(graphene.ObjectType):
    argument = graphene.String()
    type = graphene.String()

    @classmethod
    def from_dict(cls, arguments: dict) -> list[ActionArgumentNode]:
        return [
            ActionArgumentNode(
                argument=argument,
                type=type,
            )
            for argument, type in arguments.items()
        ]


class ActionSchemaNode(graphene.ObjectType):
    name = graphene.String()
    label = graphene.String()
    usage = graphene.String()
    args = graphene.List(ActionArgumentNode)

    @classmethod
    def from_action(cls, action: Action) -> ActionSchemaNode:
        action_dict = action.to_dict()
        return cls(
            name=action_dict.get("name"),
            label=action_dict.get("label"),
            usage=action_dict.get("usage"),
            args=ActionArgumentNode.from_dict(action_dict.get("args")),
        )


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="GraphQL ready!")
    actions_schema = graphene.List(ActionSchemaNode)

    def resolve_actions_schema(self, info, **kwargs):
        return [ActionSchemaNode.from_action(action) for action in TEXT_ACTIONS]


schema = graphene.Schema(query=Query)
