import graphene
from graphql_auth.schema import MeQuery, UserQuery

import ingredients.schema, user_auth.schema, social_media.schema

class Query(MeQuery,UserQuery,user_auth.schema.Query,social_media.schema.Query,graphene.ObjectType,):
    pass


class Mutation(MeQuery,UserQuery,user_auth.schema.Mutation,social_media.schema.Mutation,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)

