from django.shortcuts import render
from django.http.response import HttpResponse


def index(request):
    return render(request, 'index.html', {'nbar': '/'})


def about(request):
    return render(request, 'about.html', {'nbar': 'about'})


def agent(request):
    return render(request, 'agent.html', {'nbar': 'agent'})


def services(request):
    return render(request, 'services.html', {'nbar': 'services'})


def properties(request):
    return render(request, 'properties.html', {'nbar': 'properties'})


def blog(request):
    return render(request, 'blog.html', {'nbar': 'blog'})


def contact(request):
    return render(request, 'contact.html', {'nbar': 'contact'})
