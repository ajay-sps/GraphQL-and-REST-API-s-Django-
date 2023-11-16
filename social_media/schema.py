import graphene

from user_auth.models import User

from social_media.mutation import *
from social_media.types import *
from social_media.filter import *
from graphql_jwt.decorators import login_required


class Query(graphene.ObjectType):

    users = graphene.List(UserType)
    user_by_id = graphene.Field(UserType, id=graphene.Int(required=True))

    @login_required
    def resolve_users(self,info):
        return User.objects.all()

    @login_required
    def resolve_user_by_id(self, info, id):
        return User.objects.get(id=id)
    

class Mutation(graphene.ObjectType):
    apiCreateUser = UserSignup.Field()
    apiSignIn = UserSignIn.Field()
    create_update_employee = CreateOrUpdateEmployeeMutation.Field()

