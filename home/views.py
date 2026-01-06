from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home_view(request):

    people = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 15},
        {'name': 'Charlie', 'age': 35}, 
        {'name': 'Diana', 'age': 28}
    ]

    return render(request, 'home/index.html', context={'people': people, 'page_title': 'Home Page'})


def contact_page(request):
    context = {'page_title': 'Contact Us'}
    return render(request, 'home/contact.html', context=context)


def about_page(request):
    context = {'page_title': 'About Us'}
    return render(request, 'home/about.html', context=context)

def success_page(request):
    return HttpResponse("<h1>Success! You have reached the success page.</h1>")