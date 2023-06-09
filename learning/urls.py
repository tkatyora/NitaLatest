from django.urls import path
from . import views

urlpatterns = [
    path('newProjects',views.newProjects, name = 'newProjects'),
    path('blog',views.blog, name ='blog'),
    
    
]
