from django.shortcuts import render
from ecoverdeapp.models import Announcement


def index(request):
    baza = Announcement.objects.all()
    return render(request, 'index.html', {'baza': baza, 'nbar': 'index'} )


def about(request):
    return render(request, 'about.html', {'nbar': 'about'})


def agent(request):
    return render(request, 'agent.html', {'nbar': 'agent'})


def services(request):
    return render(request, 'services.html', {'nbar': 'services'})


def properties(request):
    return render(request, 'properties.html', {'nbar': 'properties'})


def properties_single(request):
    return render(request, 'properties-single.html')


def blog(request):
    return render(request, 'blog.html', {'nbar': 'blog'})


def blog_single(request):
    return render(request, 'blog-single.html')

def contact(request):
    return render(request, 'contact.html', {'nbar': 'contact'})
