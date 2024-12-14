from django.urls import path
from myblog.views import RecipesView,RecipeView
urlpatterns = [
    path('',RecipesView.as_view(),name='recipes'),
    path('recipe/<int:pk>',RecipeView.as_view(),name='recipe')

]
