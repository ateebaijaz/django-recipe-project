from django.shortcuts import redirect, render
from .models import *

from django.http import HttpResponse
# Create your views here.
def recipe(request):
    if request.method=="POST":
        data=request.POST
        recipe_image=request.FILES.get('recipe_image')
        recipe_name=data.get('recipe_name')
        recipe_desc=data.get('recipe_desc')

        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_image=recipe_image,
            recipe_desc=recipe_desc,
        )
        return redirect('/recipe/')
        
    queryset=Recipe.objects.all()
    context={'recipe':queryset}
    return render(request,'recipe.html',context)

def delete_recipe(request, id):
    queryset=Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipe/')

def update_recipe(request, id):
    queryset=Recipe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST

        recipe_image=request.FILES.get('recipe_image')
        recipe_name=data.get('recipe_name')
        recipe_desc=data.get('recipe_desc')

        queryset.recipe_name=recipe_name
        queryset.recipe_desc=recipe_desc

        if recipe_image:
            queryset.recipe_image=recipe_image

        queryset.save()
        return redirect('/recipe/')

    context={'recipe':queryset}
    return render(request,'update_recipe.html',context)
    


def login_page(request):
    return render(request,'login.html')


def register(request):
    if request.method == "POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user= User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )

        user.set_password(password)
        user.save()

        return redirect('/register/')

    return render(request, 'register.html')