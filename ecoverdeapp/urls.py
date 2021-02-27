from django.urls import path
from . import views

urlpatterns = [
    path('',views.index ),
    path('about', views.about),
    path('agent', views.agent),
    path('services', views.services),
    path('properties', views.properties),
    path('properties_single', views.properties_single),
    path('blog', views.blog),
    path('blog_single', views.blog_single),
    path('contact', views.contact)
]
