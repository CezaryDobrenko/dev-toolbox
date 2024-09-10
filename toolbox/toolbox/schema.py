import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="GraphQL ready!")


schema = graphene.Schema(query=Query)
