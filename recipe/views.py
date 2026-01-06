from django.shortcuts import redirect, render
from .models import Recipe
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login/")
def recipes(request):
    if request.method == 'POST':
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        print("Recipe Name:", recipe_name)
        print("Recipe Description:", recipe_description)
        print("Recipe Image:", recipe_image)

        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image
        )

        return redirect('/recipes/')
    
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        print("Search Query:", request.GET.get('search'))
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))

    context = {'recipes': queryset}
    return render(request, 'recipes.html', context)


def update_recipe(request, recipe_id):
    queryset = Recipe.objects.get(id=recipe_id)

    if request.method == 'POST':
        data = request.POST
        new_recipe_name = data.get('recipe_name')
        new_recipe_description = data.get('recipe_description')
        new_recipe_image = request.FILES.get('recipe_image')

        queryset.recipe_name = new_recipe_name
        queryset.recipe_description = new_recipe_description
        if new_recipe_image:
            queryset.recipe_image = new_recipe_image

        queryset.save()
        print(f"Recipe id: {recipe_id} updated successfully.")
        return redirect('/recipes/')

    context = {'recipe': queryset}
    return render(request, 'update_recipes.html', context)

def delete_recipe(request, recipe_id):
    queryset = Recipe.objects.get(id=recipe_id)
    queryset.delete()
    print(f"Recipe id: {recipe_id} deleted successfully.")
    return redirect('/recipes/')

def login_page(request):

    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        print("Username:", username)
        print("Password:", password)

        # Authentication logic can be added here
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid username.")
            print("Invalid username.")
            return redirect('/login/')

        user = authenticate(request=request, username=username, password=password)

        if user is None:
            messages.error(request, "Invalid password.")
            print("Invalid password.")
            return redirect('/login/')
        else:
            login(request, user)
            print("User Authenticated Successfully.")
            return redirect('/recipes/')
    
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "Username already taken. Please choose a different username.")
            print("Username already taken. Please choose a different username.")
            return redirect('/register/')

        print("First Name:", first_name)
        print("Last Name:", last_name)
        print("Username:", username)

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save()
        messages.info(request, "User registered successfully. Please login.")
        
        return redirect('/register/')
    
    return render(request, 'register.html')

def logout_page(request):

    logout(request)
    return redirect('/login/')