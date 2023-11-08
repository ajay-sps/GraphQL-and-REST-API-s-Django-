from graphene import InputObjectType, String, Int, Boolean
from graphene_django import DjangoObjectType

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from social_media.models import UserProfile

class TokenType(DjangoObjectType):
    class Meta:
        model = Token
        ields =('id', 'key', 'user')


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields =('id', 'first_name', 'last_name', 'username', 'password', 'email','auth_token', 'user_profile')



class UserProfileType(DjangoObjectType):
    class Meta:
        model = UserProfile
        fields =('id', 'bio','pincode','user')





# ==============================   Inputs  =====================================

class UserProfileInputType(InputObjectType):
    bio = String()    
    pincode = Int(required=True)


class UserInputType(InputObjectType):
    # These naming are important as if it contains unserscore here, in query we have to remove it and add camlecasing
    first_name = String()     
    username =   String()    
    userProfile = UserProfileInputType()


