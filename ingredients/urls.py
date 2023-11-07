from django.urls import path,include
from ingredients.views import Home,HomeView


urlpatterns = [
    path('',HomeView.as_view(),name="home page"),
    path('orm',Home,name='orm_testing'),
]