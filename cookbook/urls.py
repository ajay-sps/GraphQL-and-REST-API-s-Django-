"""
URL configuration for cookbook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from employee.schema import schema
from social_media.schema import schema as socialSchema
from user_auth.schema import schema as authSchema
from cookbook.schema import schema as ingeScema


urlpatterns = [
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=ingeScema))),
    path("auth", csrf_exempt(GraphQLView.as_view(graphiql=True,schema=authSchema))),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    path("social", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=socialSchema))),
    path('',include('ingredients.urls')),
]
