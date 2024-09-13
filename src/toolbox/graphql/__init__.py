import graphene

from toolbox.graphql.mutation.base import Mutation
from toolbox.graphql.schema.base import Query

schema = graphene.Schema(query=Query, mutation=Mutation)
