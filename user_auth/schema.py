from graphql_auth.schema import MeQuery, UserQuery
import graphene
from graphql_auth import mutations
from social_media.types import *
from graphql_jwt.decorators import login_required


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email  = mutations.SendPasswordResetEmail.Field()
    password_reset  = mutations.PasswordReset.Field()


class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    @login_required
    def resolve_users(self,info):
        print("=-=-auth-==-=-=")
        return User.objects.all()

class Mutation(AuthMutation, graphene.ObjectType):
    pass

