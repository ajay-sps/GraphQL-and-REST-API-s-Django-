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



# class CategoryInput(InputObjectType):
#     name = String()


# class IngredientInput(InputObjectType):
#     name = String()
#     notes = String()
#     category_id = Int()


# class CreateCategory(Mutation):
#     class Arguments:
#         input = CategoryInput()

#     ok = Boolean()
#     category = graphene.Field(CategoryNode)

#     @staticmethod
#     def mutate(root, info, input):
#         print(input)
#         serializer = CategorySerializer(data=input)
#         # if serializer.is_valid():
#         #     return True
#         category = Category(name=input.name)
#         category.save()
#         return CreateCategory(ok=True, category=category)
#         # else:
#         #     print(serializer.errors())
#         #     return "hello"
    

# class UpdateCategory(Mutation):
#     class Arguments:
#         id = Int()
#         input = CategoryInput()

#     ok = Boolean()
#     category = graphene.Field(CategoryNode)

#     @staticmethod
#     def mutate(root, info, id, input):
#         category = Category.objects.get(pk=id)
#         if input.name:
#             category.name = input.name
#         category.save()
#         return UpdateCategory(ok=True, category=category)
    

# class DeleteCategory(Mutation):
#     class Arguments:
#         id = Int()

#     ok = Boolean()

#     @staticmethod
#     def mutate(root, info, id):
#         try:
#             category = Category.objects.get(pk=id)
#             category.delete()
#             return DeleteCategory(ok=True)
#         except Category.DoesNotExist:
#             return DeleteCategory(ok=False)


# class Mutation(graphene.ObjectType):
#     create_category = CreateCategory.Field()
#     update_category = UpdateCategory.Field() 
#     delete_category = DeleteCategory.Field()


class Query(graphene.ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    ingredient = relay.Node.Field(IngredientNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode)



schema = graphene.Schema(query=Query)

# class Query(graphene.ObjectType):
    # all_ingredients = graphene.List(IngredientType)
    # category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    # def resolve_all_ingredients(root, info):
    #     # We can easily optimize query count in the resolve method
    #     return Ingredient.objects.all()

    # def resolve_category_by_name(root, info, name):
    #     try:
    #         return Category.objects.get(name=name)
    #     except Category.DoesNotExist:
    #         return None


# class CategoryType(DjangoObjectType):
#     class Meta:
#         model = Category
#         fields = ("id", "name", "ingredients")


# class IngredientType(DjangoObjectType):
#     class Meta:
#         model = Ingredient
#         fields = ("id", "name", "notes", "category")