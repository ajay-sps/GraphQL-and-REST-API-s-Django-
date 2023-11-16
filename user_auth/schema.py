from graphql_auth.schema import MeQuery, UserQuery
import graphene
from graphql_auth import mutations
from social_media.types import *


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email  = mutations.SendPasswordResetEmail.Field()
    password_reset  = mutations.PasswordReset.Field()


class Query(UserQuery,MeQuery,graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self,info):
        print("=-=-")
        return User.objects.all()

class Mutation(AuthMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query,mutation=Mutation)