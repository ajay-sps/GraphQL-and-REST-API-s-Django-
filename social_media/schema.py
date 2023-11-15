import graphene

from django.contrib.auth.models import User

from social_media.mutation import *
from social_media.types import *
from social_media.filter import *




class Query(graphene.ObjectType):
    # Define your query fields here
    users = graphene.List(UserType,filter = UserFilter())
    users_profile = graphene.List(UserProfileInputType,filter = UserProfileFilter())

    # here is a field to fetch user by ID
    user_by_id = graphene.Field(UserType,id=graphene.Int(required=True))

    def resolve_users(self, info, **kwargs):
        filters = kwargs.get('filters', {})
        return User.objects.filter(**filters)
    
    def resolve_user_profiles(self, info, **kwargs):
        filters = kwargs.get('filters', {})
        return UserProfile.objects.filter(**filters)
    
    # resolver function to fetch user with ID

    def resolve_user_by_id(self,info,id):
        return User.objects.get(id=id)
    


class Mutation(graphene.ObjectType):
    # THis name is very importanta and if you add underscoe in the name, in client side mutation query needs to remove underscore and add camer Casing there
    # eg - "api_create_User"  will be used as "apiCreateUser"
    apiCreateUser = UserSignup.Field()
    apiSignIn = UserSignIn.Field()
    create_update_employee = CreateOrUpdateEmployeeMutation.Field()

# Define the payload type


schema = graphene.Schema(query=Query,mutation=Mutation)