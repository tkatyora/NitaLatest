from django.shortcuts import render
from .models import *
# Create your views here.
# code for blogs
def blog(request):
    content={}
    return render(request , 'learning/blog.html',content)


def newProjects(request):
    return render(request , 'Nitacagra/newProjects.html')
    