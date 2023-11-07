from django.shortcuts import render
from ingredients.models import Ingredient, Category
from django.http import HttpResponse
from rest_framework.views import APIView


def Home(request):
    print(11111)
    items = Ingredient.objects.select_related("category").all()
    print(items)
    for item in items:
        print(item.category)
    return HttpResponse("Hello, this is a plain text response.")


class HomeView(APIView):

    def get(self,request):
        return render(request,'category.html')
