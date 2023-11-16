import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene import InputObjectType, Mutation
from graphene import String, Int, Boolean
from ingredients.serializer import CategorySerializer

from ingredients.models import Category, Ingredient
from graphene_django.filter import DjangoFilterConnectionField


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['id','name', 'ingredients']
        interfaces = (relay.Node, )


class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        # Allow for some more advanced filtering here
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    ingredient = relay.Node.Field(IngredientNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode)



schema = graphene.Schema(query=Query)

