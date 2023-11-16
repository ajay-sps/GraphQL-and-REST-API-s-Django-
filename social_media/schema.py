import graphene

from user_auth.models import User

from social_media.mutation import *
from social_media.types import *
from social_media.filter import *
from graphql_auth.schema import MeQuery, UserQuery



class Query(UserQuery,MeQuery,graphene.ObjectType):
    # Define your query fields here
    # users = graphene.List(UserType, filters=graphene.Argument(UserFilter))
    # user_profiles = graphene.List(UserProfileType, filters=graphene.Argument(UserProfileFilter))
    users = graphene.List(UserType)

    # Field to fetch user by ID
    user_by_id = graphene.Field(UserType, id=graphene.Int(required=True))

    # def resolve_users(self, info, filters=None, **kwargs):
    #     print(111)
    #     return User.objects.filter(**filters)

    def resolve_users(self,info):
        return User.objects.all()

    def resolve_user_profiles(self, info, filters=None, **kwargs):
        return UserProfile.objects.filter(**filters)

    # Resolver function to fetch user with ID
    def resolve_user_by_id(self, info, id):
        return User.objects.get(id=id)
    


class Mutation(graphene.ObjectType):
    # THis name is very importanta and if you add underscoe in the name, in client side mutation query needs to remove underscore and add camer Casing there
    # eg - "api_create_User"  will be used as "apiCreateUser"
    apiCreateUser = UserSignup.Field()
    apiSignIn = UserSignIn.Field()
    create_update_employee = CreateOrUpdateEmployeeMutation.Field()

# Define the payload type


schema = graphene.Schema(query=Query,mutation=Mutation)