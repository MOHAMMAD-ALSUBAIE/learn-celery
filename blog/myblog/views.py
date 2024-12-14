from django.shortcuts import render
from django.views.generic import ListView,View
# Create your views here.
from django.http import  HttpResponse
from django.core.cache import cache
from myblog.models import Recipe
class RecipesView(ListView):
    queryset=Recipe.objects.all()
    context_object_name='recipes'
    template_name='recipes/recipes.html'

class RecipeView(View):
    def get(self, request, *args, **kwargs):

       pk=kwargs.get("pk")
       print(pk)
       try:
         recipe=cache.get(pk)
         if recipe:
            print(recipe,'from cache')
            return HttpResponse(recipe)
         else:
          recipe=Recipe.objects.get(id=pk)
          cache.set(pk,recipe)
       except Recipe.DoesNotExist:
         pass
       return HttpResponse(recipe)
# use cache.get to retrive from cache by key
# use cache.set to store in cache