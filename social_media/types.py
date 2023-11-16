from graphene import InputObjectType, String, Int, Boolean
from graphene_django import DjangoObjectType
import graphene

from user_auth.models import User
from rest_framework.authtoken.models import Token
from social_media.models import UserProfile

from social_media.models import Employee


class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee
        fields = ('id', 'name', 'salary')

    above_50000 = graphene.Boolean()

    def resolve_above_50000(self, info):
        salary = self.salary
        return salary > 50000
                                                                                                    

class TokenType(DjangoObjectType):                    
    class Meta:
        model = Token
        fields =( 'key', 'user')


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields =('id', 'first_name', 'last_name', 'username', 'password', 'email','auth_token', 'user_profile')


    new_field = graphene.String()

    def resolve_new_field(self,info):
        id = self.id
        if id%2 == 1:
            return "Odd"
        else:
            return "Even"



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
    first_name = String(required=True)   
    username =   String(required=True)   
    password = String(required=True)
    userProfile = UserProfileInputType()


class SignInInputType(InputObjectType):

    username = String(required=True)
    password = String(required=True)

