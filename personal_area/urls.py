from django.urls import path
from . import views

urlpatterns = [
    path('', views.person, name='person'),
    path('add', views.add, name='add')    
]
