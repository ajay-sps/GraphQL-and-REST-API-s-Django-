import graphene
from graphene import  Mutation
from graphene import String, Int, Boolean

from social_media.types import UserInputType, UserType

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token





class UserSignup(Mutation):
    class Arguments:
        input = UserInputType()  

    status = Int()
    user = graphene.Field(UserType) 


    @staticmethod
    def mutate(root, info, input):
        print(input,"------------")
        user = User(**input,is_active=1)
        user.save()
        Token.objects.get_or_create(user=user)
        return UserSignup(status=201, user=user)
