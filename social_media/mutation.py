import graphene
from graphene import  Mutation
from graphene import String, Int, Boolean

from social_media.types import *

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from social_media.models import UserProfile

from django.contrib.auth import authenticate
from graphene_django.rest_framework.mutation import SerializerMutation
from social_media.serializer import EmployeeSerializer



class UserSignup(Mutation):
    class Arguments:
        input = UserInputType()  

    status = Int()
    user = graphene.Field(UserType) 


    @staticmethod
    def mutate(root, info, input):
        print(input,"------------")
        profile_data = input.pop('userProfile')
        password = input.pop('password')
        user = User(**input,is_active=1)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(**profile_data,user=user)
        Token.objects.get_or_create(user=user)
        return UserSignup(status=201, user=user)


class UserSignIn(Mutation):
    class Arguments:
        req_data = SignInInputType()

    status = Int()
    user = graphene.Field(UserType)
    message = String()

    @staticmethod
    def mutate(root,info,req_data):
        print(req_data,"-----------------------")
        user = authenticate(**req_data)
        if user is not None:
            Token.objects.get_or_create(user=user)
            return UserSignIn(status=200,user=user,message="success")
        else:
            return UserSignIn(status=400,user = None,message="User not found")
        

class CreateOrUpdateEmployeeMutation(SerializerMutation):
    employee = graphene.Field(EmployeeType)

    class Meta:                           
        serializer_class = EmployeeSerializer
        model_operations = ['create', 'update']

    # @classmethod
    # def perform_mutate(cls, serializer, info):
    #     print("Performing mutate...")
    #     instance = super().perform_mutate(serializer, info)
    #     print("Instance:", instance)
    #     return cls(employee=instance)
        