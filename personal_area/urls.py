from django.urls import path
from . import views


urlpatterns = [
    path('', views.personal, name='personal'),
    path('add', views.add, name='add'),   
    
]
