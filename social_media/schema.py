import graphene

from django.contrib.auth.models import User

from social_media.mutation import *
from social_media.types import *






class Query(graphene.ObjectType):
    # Define your query fields here
    users = graphene.List(UserType)

    def resolve_users(self, info):
        # Define how to resolve the query for all departments
        return User.objects.all()
    

class Mutation(graphene.ObjectType):
    # THis name is very importanta and if you add underscoe in the name, in client side mutation query needs to remove underscore and add camer Casing there
    # eg - "api_create_User"  will be used as "apiCreateUser"
    apiCreateUser = UserSignup.Field()


schema = graphene.Schema(query=Query,mutation=Mutation)