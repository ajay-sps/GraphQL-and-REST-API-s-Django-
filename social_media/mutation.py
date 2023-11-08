import graphene
from graphene import  Mutation
from graphene import String, Int, Boolean

from social_media.types import UserInputType, UserType

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from social_media.models import UserProfile





class UserSignup(Mutation):
    class Arguments:
        input = UserInputType()  

    status = Int()
    user = graphene.Field(UserType) 


    @staticmethod
    def mutate(root, info, input):
        print(input,"------------")
        profile_data = input.pop('userProfile')
        user = User(**input,is_active=1)
        user.save()
        UserProfile.objects.create(**profile_data,user=user)
        Token.objects.get_or_create(user=user)
        return UserSignup(status=201, user=user)
