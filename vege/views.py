from django.shortcuts import render, redirect
from .models import*
from django.http import HttpResponse
# Create your views here.
def recipes(request):
    if(request.method == 'POST'):
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')
        
        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image,
        )

        return redirect('/recipes/')

    queryset = Recipe.objects.all() 

    #####################################

    if request.GET.get('search'):
        #print(request.GET.get('search'))
        queryset = queryset.filter(recipe_name__icontains=request.GET.get('search'))

    ###########---------------------------------------------

    context = {'recipes': queryset}   
    return render(request, 'recipes.html', context)

def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    #return HttpResponse("a")
    return redirect('/recipes/')

def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    if(request.method == 'POST'):
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')
        
        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        if recipe_image:
            queryset.recipe_image = recipe_image
        queryset.save()
        return redirect('/recipes/')

    
    context = {'recipe': queryset} 
    return render(request, 'update_recipes.html', context)