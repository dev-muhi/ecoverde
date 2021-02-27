from django.urls import path
from . import views

urlpatterns = [
    path('',views.index ),
    path('about', views.about),
    path('agent', views.agent),
    path('services', views.services),
    path('properties', views.properties),
    path('blog', views.blog),
    path('contact', views.contact)
]
