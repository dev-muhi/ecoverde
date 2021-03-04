from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('agent', views.agent, name = 'agent'),
    path('services', views.services, name='services'),
    path('properties', views.properties, name='properties'),
    path('properties_single', views.properties_single, name = 'properties_single' ),
    path('blog', views.blog, name='blog'),
    path('blog_single', views.blog_single, name='blog_single'),
    path('contact', views.contact, name='contact')
   
]
