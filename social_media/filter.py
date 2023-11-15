import django_filters
from social_media.models import *
from django.contrib.auth.models import User


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username','email']


class UserProfileFilter(django_filters.FilterSet):
    # user = django_filters.NestedFilter(UserFilter, field_name='user')

    class Meta:
        model = UserProfile
        fields = ['bio','pincode','user']

