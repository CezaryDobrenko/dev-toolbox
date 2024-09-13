from __future__ import annotations

import graphene

from toolbox.actions.action import Action


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
